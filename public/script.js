// Growth Engine - Frontend JavaScript

document.addEventListener("DOMContentLoaded", () => {
  const API_ENDPOINT = "/invoke";
  const PDF_ENDPOINT = "/generate-pdf";

  // Form elements
  const form = document.getElementById("analysis-form");
  const submitButton = document.getElementById("submit-button");
  const urlInput = document.getElementById("url");
  const errorMessage = document.getElementById("form-error");

  // View sections
  const heroSection = document.getElementById("hero-banner");
  const comoFuncionaSection = document.getElementById("como-funciona");
  const featuresSection = document.getElementById("features");
  const loader = document.getElementById("loader");
  const dashboardSection = document.getElementById("dashboard-section");
  const footer = document.querySelector(".site-footer");

  // Dashboard elements
  const reportUrl = document.getElementById("report-url");
  const reportContent = document.getElementById("report-content");
  const backButton = document.getElementById("back-button");
  const downloadButton = document.getElementById("download-button");

  let currentMarkdownReport = "";
  let currentUrl = "";

  /**
   * Show specific view and hide others
   */
  function showView(view) {
    // Hide all main sections
    if (heroSection) heroSection.classList.add("hidden");
    if (comoFuncionaSection) comoFuncionaSection.classList.add("hidden");
    if (featuresSection) featuresSection.classList.add("hidden");
    if (loader) loader.classList.add("hidden");
    if (dashboardSection) dashboardSection.classList.add("hidden");
    if (footer) footer.classList.add("hidden");

    // Show requested view
    if (view === "hero") {
      if (heroSection) heroSection.classList.remove("hidden");
      if (comoFuncionaSection) comoFuncionaSection.classList.remove("hidden");
      if (featuresSection) featuresSection.classList.remove("hidden");
      if (footer) footer.classList.remove("hidden");
    } else if (view === "loader") {
      if (loader) loader.classList.remove("hidden");
    } else if (view === "dashboard") {
      if (dashboardSection) dashboardSection.classList.remove("hidden");
      if (footer) footer.classList.remove("hidden");

      // Scroll to top when showing dashboard
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  }

  /**
   * Show error message
   */
  function setFormError(message) {
    if (errorMessage) {
      errorMessage.textContent = message;
      errorMessage.classList.remove("hidden");
    }
  }

  /**
   * Clear error message
   */
  function clearFormError() {
    if (errorMessage) {
      errorMessage.classList.add("hidden");
    }
  }

  /**
   * Handle form submission and analysis
   */
  async function handleAnalysis(event) {
    event.preventDefault();
    clearFormError();

    let url = urlInput.value.trim();
    if (!url) {
      setFormError("Por favor, insira uma URL válida.");
      return;
    }

    // Add https:// if not present
    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      url = "https://" + url;
    }

    currentUrl = url;

    // Update button state
    submitButton.disabled = true;
    const originalButtonText = submitButton.innerHTML;
    submitButton.innerHTML = '<span>Analisando...</span>';

    // Show loader
    showView("loader");

    try {
      console.log("[INFO] Enviando requisição para:", API_ENDPOINT);
      console.log("[INFO] URL a ser analisada:", currentUrl);

      const response = await fetch(API_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: currentUrl }),
      });

      console.log("[INFO] Status da resposta:", response.status);

      if (!response.ok) {
        let errorText = `Erro ${response.status}`;
        try {
          const errorData = await response.json();
          errorText = errorData.error || errorText;
        } catch (e) {
          errorText = await response.text();
        }
        throw new Error(errorText);
      }

      const result = await response.json();
      console.log("[INFO] Resposta recebida com sucesso");

      if (!result.output) {
        throw new Error("O servidor não retornou um relatório válido.");
      }

      // Store report and display
      currentMarkdownReport = result.output;
      reportContent.innerHTML = marked.parse(currentMarkdownReport);
      reportUrl.textContent = currentUrl;

      console.log("[INFO] Relatório renderizado com sucesso");
      showView("dashboard");

    } catch (error) {
      console.error("[ERROR] Falha ao buscar análise:", error);

      let userMessage = "Não foi possível gerar a análise. ";

      if (error.message.includes("Failed to fetch") || error.message.includes("NetworkError")) {
        userMessage += "Verifique sua conexão com a internet.";
      } else if (error.message.includes("GOOGLE_API_KEY")) {
        userMessage += "Erro de configuração do servidor (API key).";
      } else if (error.message.includes("404")) {
        userMessage += "Modelo de IA não encontrado. Contate o suporte.";
      } else {
        userMessage += error.message;
      }

      setFormError(userMessage);
      showView("hero");

    } finally {
      // Reset button state
      submitButton.disabled = false;
      submitButton.innerHTML = originalButtonText;
    }
  }

  /**
   * Handle PDF download
   */
  async function handleDownload() {
    if (!currentMarkdownReport || !currentUrl) {
      alert("Nenhum relatório disponível para download.");
      return;
    }

    downloadButton.disabled = true;
    const originalButtonHTML = downloadButton.innerHTML;
    downloadButton.innerHTML = `
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"></circle>
      </svg>
      <span>Gerando PDF...</span>
    `;

    try {
      console.log("[INFO] Solicitando geração de PDF...");

      const response = await fetch(PDF_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          markdown: currentMarkdownReport,
          url: currentUrl,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.error || `Erro ${response.status} ao gerar PDF`);
      }

      // Download the PDF
      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = downloadUrl;

      // Create filename from URL
      const safeUrl = currentUrl
        .replace(/https?:\/\//, "")
        .replace(/[^a-z0-9]/gi, "_")
        .substring(0, 30);
      a.download = `growth_engine_relatorio_${safeUrl}.pdf`;

      document.body.appendChild(a);
      a.click();

      // Cleanup
      window.URL.revokeObjectURL(downloadUrl);
      document.body.removeChild(a);

      console.log("[INFO] PDF baixado com sucesso");

    } catch (error) {
      console.error("[ERROR] Erro ao baixar PDF:", error);

      let errorMsg = "Erro ao gerar PDF. ";
      if (error.message.includes("503")) {
        errorMsg += "A geração de PDF está temporariamente indisponível. Use 'Copiar' para salvar o relatório.";
      } else {
        errorMsg += error.message;
      }

      alert(errorMsg);

    } finally {
      downloadButton.disabled = false;
      downloadButton.innerHTML = originalButtonHTML;
    }
  }

  /**
   * Handle back button - return to hero
   */
  function handleBack() {
    // Clear current report
    currentMarkdownReport = "";
    currentUrl = "";
    reportContent.innerHTML = "";
    reportUrl.textContent = "";
    urlInput.value = "";
    clearFormError();

    // Show hero view
    showView("hero");

    // Scroll to top
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  // Event listeners
  if (form) {
    form.addEventListener("submit", handleAnalysis);
  }

  if (backButton) {
    backButton.addEventListener("click", handleBack);
  }

  if (downloadButton) {
    downloadButton.addEventListener("click", handleDownload);
  }

  // Smooth scroll for navigation links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const targetId = this.getAttribute("href");
      const targetElement = document.querySelector(targetId);

      if (targetElement) {
        const headerOffset = 80;
        const elementPosition = targetElement.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: "smooth"
        });
      }
    });
  });

  // Initialize view
  showView("hero");

  console.log("[INFO] Growth Engine inicializado com sucesso");
});
