(() => {
  const form = document.querySelector("[data-diagnostic-form]");
  if (!form) return;

  const whatsappNumber = ""; // PREENCHER: número oficial, apenas dígitos com código do país.
  const submitButton = form.querySelector("[data-whatsapp-submit]");
  const status = form.querySelector("[data-form-status]");
  const destinationIsConfigured = /^\d{10,15}$/.test(whatsappNumber);

  const announce = (message) => {
    if (!status) return;
    status.textContent = message;
    status.hidden = false;
  };

  if (submitButton) submitButton.disabled = !destinationIsConfigured;
  if (!destinationIsConfigured) {
    announce("O canal de WhatsApp da Vision ainda precisa ser configurado. Nenhum dado foi enviado.");
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const trap = form.elements.namedItem("company-website");
    if (trap && trap.value.trim()) {
      announce("Não foi possível processar este pedido. Revise a página e tente novamente.");
      return;
    }

    if (!destinationIsConfigured) {
      announce("O WhatsApp oficial da Vision ainda não foi configurado. Nenhum dado foi enviado.");
      return;
    }

    const values = new FormData(form);
    const get = (key) => String(values.get(key) || "").trim();
    const lines = [
      "Olá! Gostaria de pedir um diagnóstico para minha empresa.",
      `Nome: ${get("name")}`,
      `Empresa: ${get("company")}`
    ];
    if (get("site")) lines.push(`Site ou Instagram: ${get("site")}`);
    if (get("objective")) lines.push(`O que gostaria de melhorar: ${get("objective")}`);
    lines.push("Mensagem preparada no site da Vision; vou revisar antes de enviar.");
    const message = lines.join("\n");

    const url = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
    window.location.assign(url);
  });
})();
