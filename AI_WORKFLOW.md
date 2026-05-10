# AI workflow prompts for building the portfolio

Use this as your step-by-step script when asking AI for help. Each step includes what you should ask, the kind of answer you want, and common mistakes to avoid.

## Step 1: Create the main GitHub Pages repo

Ask AI:

```text
Help me create one GitHub Pages portfolio repository named christopherbarker.github.io. Give me the exact steps for GitHub desktop or terminal, and explain where my website files should go.
```

Good answer:

Create one repo named `christopherbarker.github.io`. Put `index.html`, `projects.html`, `resume.html`, `contact.html`, folders, and assets at the root of that repo. GitHub Pages will publish it at `https://christopherbarker.github.io`.

Common mistakes:

- Naming the repo something like `portfolio` and expecting the same URL.
- Uploading the whole parent folder so the homepage is hidden inside `portfolio-site/`.
- Making separate portfolio sites for every class project.

## Step 2: Build the website structure

Ask AI:

```text
Create a clean GitHub Pages portfolio structure with index, projects, resume, contact, css, js, images, assets, featured, supporting, and resume folders.
```

Good answer:

Use a shallow structure with simple top navigation: Home, Projects, Resume, Contact. Keep project pages inside `featured/`, supporting work inside `supporting/`, and downloadable files inside `assets/` or `resume/`.

Common mistakes:

- Deep menus with too many categories.
- Making reviewers click through several pages before seeing work.
- Mixing raw notebooks, PDFs, screenshots, and site files without clean folders.

## Step 3: Curate the homepage

Ask AI:

```text
Design my homepage so it only has a short intro, hero image, 4 to 6 featured project cards, resume button, and contact button.
```

Good answer:

Homepage should feel visual and quick. It should show Christopher Barker, a short positioning sentence, a strong project collage, and selected featured work. The homepage should not be an archive.

Common mistakes:

- Listing every assignment on the homepage.
- Using giant paragraphs before showing project images.
- Adding a complicated bio before the reviewer sees the work.

## Step 4: Build featured project pages

Ask AI:

```text
For each featured project, create a concise case study page with title, summary, technologies, screenshots, problem, process, outcome, and GitHub link placeholder.
```

Good answer:

Each page should be scannable. Use short sections, project screenshots, and a clear link to code or demo. The featured projects come from the `featured_projects` source folder: Opioid Prescribing Risk Analysis, Grocery Retail Consumer Analytics, Minesweeper Game, Battleship Game, HTML Resume Portfolio, AI Caption Generator, GAN Discord Bot, and Data Collaboration Room Studio.

Common mistakes:

- Writing long school-assignment explanations.
- Forgetting screenshots.
- Linking only to a download file instead of a repo or live demo.

## Step 5: Move supporting work into an archive

Ask AI:

```text
Create a compact supporting work section for extra class projects so they do not clutter the homepage.
```

Good answer:

Use one archive section with short descriptions. Supporting work should show range but stay secondary.

Common mistakes:

- Treating every project as equally important.
- Making supporting work visually louder than featured work.
- Including unfinished files without context.

## Step 6: Polish branding

Ask AI:

```text
Apply one consistent portfolio identity using dark navy, cream/off-white, and one muted accent color. Keep typography, cards, buttons, and spacing consistent across all pages.
```

Good answer:

The whole site should feel like one professional portfolio, even though the projects span AI, design, frontend, and research.

Common mistakes:

- Different colors and styles on every project page.
- Too many accent colors.
- Making the site look like a class folder instead of a curated portfolio.

## Step 7: Finish deployment details

Ask AI:

```text
Review my portfolio before I publish it. Check links, image paths, resume PDF, project pages, mobile layout, and missing placeholders.
```

Good answer:

AI should list broken links, placeholders, missing images, missing repo links, missing live demos, and any layout problems.

Common mistakes:

- Publishing before replacing placeholder email.
- Not testing on mobile.
- Forgetting to add README files to separate project repos.
- Leaving project pages without GitHub links or screenshots.
