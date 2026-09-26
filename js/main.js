for (const button of document.querySelectorAll("[data-copy]")) {
  const initialLabel = button.textContent;
  let resetTimer;
  button.addEventListener("click", async () => {
    const status = button.closest(".install").querySelector(".copy-status");
    clearTimeout(resetTimer);
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      button.textContent = button.dataset.copied;
      status.textContent = button.dataset.copied;
    } catch {
      status.textContent = button.dataset.error;
    }
    resetTimer = setTimeout(() => {
      button.textContent = initialLabel;
      status.textContent = "";
    }, 3500);
  });
}
