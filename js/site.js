document.documentElement.classList.add("js-enabled");

document.querySelectorAll(".reel-shell").forEach((shell) => {
  const reel = shell.querySelector("[data-reel]");
  const prev = shell.querySelector("[data-reel-prev]");
  const next = shell.querySelector("[data-reel-next]");

  if (!reel || !prev || !next) return;

  const move = (direction) => {
    const card = reel.querySelector(".project-card");
    const styles = window.getComputedStyle(reel);
    const gap = parseFloat(styles.columnGap);
    const distance = card
      ? card.getBoundingClientRect().width + (Number.isNaN(gap) ? 0 : gap)
      : reel.clientWidth * 0.8;
    reel.scrollBy({ left: direction * distance, behavior: "smooth" });
  };

  prev.addEventListener("click", () => move(-1));
  next.addEventListener("click", () => move(1));
});

const badgeTone = (label) => {
  const value = label.toLowerCase();
  if (value.includes("featured")) return "featured";
  if (value.includes("complete")) return "complete";
  if (value.includes("archived")) return "archived";
  if (value.includes("experimental") || value.includes("in progress")) return "experimental";
  if (value.includes("research")) return "research";
  if (value.includes("ai") || value.includes("ml") || value.includes("notebook") || value.includes("data")) return "data";
  if (value.includes("java") || value.includes("processing") || value.includes("code") || value.includes("algorithm")) return "code";
  if (value.includes("design") || value.includes("pdf") || value.includes("typography") || value.includes("editorial") || value.includes("packaging")) return "design";
  if (value.includes("documentary") || value.includes("video") || value.includes("animation") || value.includes("campaign") || value.includes("sticker")) return "media";
  return "neutral";
};

document.querySelectorAll(".archive-item > span").forEach((metadata) => {
  const labels = metadata.textContent
    .split("/")
    .map((label) => label.trim())
    .filter(Boolean)
    .filter((label, index) => !(index === 0 && label.toLowerCase() === "supporting"));

  if (labels.length < 2) return;

  const badges = document.createElement("span");
  badges.className = "meta-badges";

  labels.forEach((label) => {
    const badge = document.createElement("span");
    badge.className = `meta-badge meta-${badgeTone(label)}`;
    badge.textContent = label;
    badges.appendChild(badge);
  });

  metadata.replaceWith(badges);
});
