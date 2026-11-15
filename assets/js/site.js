(() => {
  const menuButton = document.querySelector("[data-menu-toggle]");
  const navigation = document.querySelector("[data-primary-nav]");

  if (menuButton && navigation) {
    const setMenuOpen = (isOpen) => {
      menuButton.setAttribute("aria-expanded", String(isOpen));
      menuButton.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");
      navigation.dataset.open = String(isOpen);
    };

    menuButton.addEventListener("click", () => {
      setMenuOpen(menuButton.getAttribute("aria-expanded") !== "true");
    });

    navigation.addEventListener("click", (event) => {
      if (event.target.closest("a")) setMenuOpen(false);
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
        setMenuOpen(false);
        menuButton.focus();
      }
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 760) setMenuOpen(false);
    });
  }

  document.querySelectorAll("[data-current-year]").forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });

  const motionPreference = window.matchMedia("(prefers-reduced-motion: reduce)");
  const page = document.body.dataset.page || "";
  const sceneMap = {
    home: ["night", "plum", "paper", "smoke", "night", "ember"],
    agency: ["night", "paper", "plum", "ember"],
    sites: ["night", "paper", "smoke", "ember"],
    seo: ["night", "paper", "plum", "ember"],
    intelligence: ["night", "plum", "paper", "ember"],
    projects: ["night", "paper", "night"],
    diagnostic: ["night", "paper", "plum"],
    legal: ["night"],
    notfound: ["night"]
  };
  const sections = [...document.querySelectorAll("main > section")];
  const scenes = sceneMap[page] || ["night"];
  sections.forEach((section, index) => {
    if (!section.dataset.scene) section.dataset.scene = scenes[Math.min(index, scenes.length - 1)] || "night";
  });

  const applyScene = (scene) => {
    const currentScene = scene || "night";
    document.body.dataset.scene = currentScene;
    document.documentElement.style.colorScheme = currentScene === "paper" ? "light" : "dark";
  };
  applyScene(document.body.dataset.scene);

  const updateScene = (entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (visible) applyScene(visible.target.dataset.scene);
  };

  if ("IntersectionObserver" in window && sections.length) {
    const sceneObserver = new IntersectionObserver(updateScene, {
      threshold: [0.12, 0.28, 0.48, 0.68],
      rootMargin: "-14% 0px -32% 0px"
    });
    sections.forEach((section) => sceneObserver.observe(section));
  }

  const revealSelectors = [
    ".hero-copy", ".home-signal", ".home-proof", ".section-heading", ".contrast-card",
    ".service-card", ".method-step", ".project-card", ".service-layout",
    ".value-card", ".diagnostic-aside", ".form-card", ".cta-panel", ".intelligence-hero-art"
  ].join(",");
  const revealNodes = [...document.querySelectorAll(revealSelectors)];
  const typewriterNodes = [...document.querySelectorAll("[data-typewriter]")];
  const canAnimate = !motionPreference.matches && "IntersectionObserver" in window;

  if (canAnimate && (revealNodes.length || typewriterNodes.length)) {
    document.documentElement.classList.add("js-motion");
    revealNodes.forEach((element, index) => {
      element.dataset.reveal = "";
      element.style.setProperty("--reveal-delay", `${Math.min(index % 4, 3) * 75}ms`);
    });

    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.14, rootMargin: "0px 0px -7% 0px" });
    revealNodes.forEach((element) => revealObserver.observe(element));

    const typeText = (element) => {
      if (element.dataset.typed === "true") return;
      element.dataset.typed = "true";
      const fullText = element.dataset.text || element.textContent.trim();
      element.textContent = "";
      let position = 0;
      const step = () => {
        element.textContent = fullText.slice(0, position + 1);
        position += 1;
        if (position < fullText.length) window.setTimeout(step, 33);
        else element.classList.add("is-done");
      };
      step();
    };

    const typeObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        typeText(entry.target);
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.7 });

    typewriterNodes.forEach((element) => {
      if (!element.dataset.text) element.dataset.text = element.textContent.trim();
      typeObserver.observe(element);
    });
  } else {
    typewriterNodes.forEach((element) => element.classList.add("is-done"));
  }
})();
