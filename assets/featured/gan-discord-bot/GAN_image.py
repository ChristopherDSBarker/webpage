# gan_discord_bot.py
# ----------------------------
# Single-file GAN + Discord Bot
# Trains minimal CIFAR-10 horse GAN if needed
# Then listens for Discord messages to generate images
# ----------------------------
# Requirements:
# pip install torch torchvision discord.py pillow

import os
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.utils import save_image
import discord
from discord.ext import commands

# ----------------------------
# CONFIG
# ----------------------------
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
Z_DIM = 100
BATCH_SIZE = 128
LR = 0.0002
EPOCHS = 10  # Minimal proof-of-concept
GEN_PATH = "generator.pth"
DISCORD_TOKEN = "token"
OUTPUT_IMAGE = "bot_output.png"

# ----------------------------
# GENERATOR / DISCRIMINATOR
# ----------------------------
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.ConvTranspose2d(Z_DIM, 256, 4, 1, 0, bias=False),
            nn.BatchNorm2d(256), nn.ReLU(True),
            nn.ConvTranspose2d(256, 128, 4, 2, 1, bias=False),
            nn.BatchNorm2d(128), nn.ReLU(True),
            nn.ConvTranspose2d(128, 64, 4, 2, 1, bias=False),
            nn.BatchNorm2d(64), nn.ReLU(True),
            nn.ConvTranspose2d(64, 3, 4, 2, 1, bias=False),
            nn.Tanh()
        )
    def forward(self, z): return self.net(z)

class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 64, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, True),
            nn.Conv2d(64, 128, 4, 2, 1, bias=False),
            nn.BatchNorm2d(128), nn.LeakyReLU(0.2, True),
            nn.Conv2d(128, 256, 4, 2, 1, bias=False),
            nn.BatchNorm2d(256), nn.LeakyReLU(0.2, True),
            nn.Conv2d(256, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )
    def forward(self, x): return self.net(x)

# ----------------------------
# TRAINING FUNCTION
# ----------------------------
def train_gan():
    print("DOWNLOAD: CIFAR-10 dataset...")
    dataset = dset.CIFAR10(root='./data', train=True, download=True,
                           transform=transforms.Compose([
                               transforms.Resize(32),
                               transforms.ToTensor(),
                               transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
                           ]))
    
    idx = [i for i, (_, label) in enumerate(dataset) if label==7]
    horse_set = torch.utils.data.Subset(dataset, idx)
    dataloader = DataLoader(horse_set, batch_size=BATCH_SIZE, shuffle=True)

    netG = Generator().to(DEVICE)
    netD = Discriminator().to(DEVICE)
    optD = optim.Adam(netD.parameters(), lr=LR, betas=(0.5,0.999))
    optG = optim.Adam(netG.parameters(), lr=LR, betas=(0.5,0.999))
    criterion = nn.BCELoss()

    print("TRAIN: Starting training loop...")
    for epoch in range(EPOCHS):
        for i, (data, _) in enumerate(dataloader):
            # Update D
            netD.zero_grad()
            real = data.to(DEVICE)
            b_size = real.size(0)
            label = torch.ones(b_size, device=DEVICE)
            output = netD(real).view(-1)
            errD_real = criterion(output, label)
            errD_real.backward()
            
            noise = torch.randn(b_size, Z_DIM, 1, 1, device=DEVICE)
            fake = netG(noise)
            label.fill_(0)
            output = netD(fake.detach()).view(-1)
            errD_fake = criterion(output, label)
            errD_fake.backward()
            optD.step()

            # Update G
            netG.zero_grad()
            label.fill_(1)
            output = netD(fake).view(-1)
            errG = criterion(output, label)
            errG.backward()
            optG.step()
        print(f"Epoch {epoch+1}/{EPOCHS} complete.")
    torch.save(netG.state_dict(), GEN_PATH)
    print(f"DONE: Saved {GEN_PATH}")

# ----------------------------
# DISCORD BOT FUNCTION
# ----------------------------
def run_bot():
    generator = Generator().to(DEVICE)
    generator.load_state_dict(torch.load(GEN_PATH, map_location=DEVICE))
    generator.eval()
    print("✅ Generator loaded, starting Discord bot...")

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!gen ", intents=intents)

    @bot.event
    async def on_ready():
        print(f"Bot logged in as {bot.user}")

    @bot.event
    async def on_message(message):
        if message.author.bot: return
        content = message.content.lower()
        if "horse" in content:
            await message.channel.send("🎨 pic please")
            z = torch.randn(1, Z_DIM, 1, 1).to(DEVICE)
            with torch.no_grad():
                img = generator(z)
            save_image(img, OUTPUT_IMAGE, normalize=True)
            await message.channel.send(file=discord.File(OUTPUT_IMAGE))
        await bot.process_commands(message)

    bot.run(DISCORD_TOKEN)

# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    if not os.path.exists(GEN_PATH):
        train_gan()
    run_bot()
