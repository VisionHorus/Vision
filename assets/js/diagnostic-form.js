(() => {
  const form = document.querySelector("[data-diagnostic-form]");
  if (!form) return;

  const whatsappNumber = "000000000";

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const values = new FormData(form);
    const get = (key) => String(values.get(key) || "").trim() || "Não informado";
    const message = [
      "Olá! Gostaria de solicitar um diagnóstico digital.",
      "",
      `Nome: ${get("name")}`,
      `Empresa: ${get("company")}`,
      `Segmento: ${get("segment")}`,
      `Site ou Instagram: ${get("site")}`,
      `Meu WhatsApp: ${get("whatsapp")}`,
      `Principal dificuldade ou objetivo: ${get("objective")}`
    ].join("\n");

    const url = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
    window.location.assign(url);
  });
})();
