// public/script.js

document.addEventListener("DOMContentLoaded", () => {
  const API_ENDPOINT = "/invoke";
  const PDF_ENDPOINT = "/generate-pdf";

  const form = document.getElementById("analysis-form");
  const submitButton = document.getElementById("submit-button");
  const urlInput = document.getElementById("url");
  const errorMessage = document.getElementById("form-error");

  const heroSection = document.getElementById("hero-section");
  const loader = document.getElementById("loader");
  const dashboardSection = document.getElementById("dashboard-section");

  const reportUrl = document.getElementById("report-url");
  const reportContent = document.getElementById("report-content");
  const backButton = document.getElementById("back-button");
  const downloadButton = document.getElementById("download-button");

  let currentMarkdownReport = "";
  let currentUrl = "";

  function showView(view) {
    heroSection.classList.add("hidden");
    loader.classList.add("hidden");
    dashboardSection.classList.add("hidden");

    if (view === "hero") heroSection.classList.remove("hidden");
    else if (view === "loader") loader.classList.remove("hidden");
    else if (view === "dashboard") dashboardSection.classList.remove("hidden");
  }

  function setFormError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove("hidden");
  }

  function clearFormError() {
    errorMessage.classList.add("hidden");
  }

  async function handleAnalysis(event) {
    event.preventDefault();
    clearFormError();

    let url = urlInput.value.trim();
    if (!url) {
      setFormError("Por favor, insira uma URL.");
      return;
    }

    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      url = "https://" + url;
    }

    currentUrl = url;
    submitButton.disabled = true;
    submitButton.textContent = "Analisando...";
    showView("loader");

    try {
      const response = await fetch(API_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: currentUrl }),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Erro na API: ${response.status} - ${errorText}`);
      }

      const result = await response.json();

      if (!result.output) {
        throw new Error("A API não retornou um 'output'.");
      }

      currentMarkdownReport = result.output;
      reportContent.innerHTML = marked.parse(currentMarkdownReport);
      reportUrl.textContent = currentUrl;
      showView("dashboard");
    } catch (error) {
      console.error("Falha ao buscar análise:", error);
      setFormError(
        "Não foi possível gerar a análise. Verifique o console ou se o backend está rodando."
      );
      showView("hero");
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = "Analisar";
    }
  }

  async function handleDownload() {
    if (!currentMarkdownReport || !currentUrl) {
      alert("Nenhum relatório disponível para download.");
      return;
    }

    downloadButton.disabled = true;
    downloadButton.textContent = "Gerando PDF...";

    try {
      const response = await fetch(PDF_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          markdown: currentMarkdownReport,
          url: currentUrl,
        }),
      });

      if (!response.ok) {
        throw new Error("Erro ao gerar PDF");
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `relatorio_${currentUrl
        .replace(/https?:\/\//, "")
        .substring(0, 30)}.pdf`;
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      document.body.removeChild(a);
    } catch (error) {
      console.error("Erro ao baixar PDF:", error);
      alert("Erro ao gerar PDF. Tente novamente.");
    } finally {
      downloadButton.disabled = false;
      downloadButton.textContent = "Baixar PDF";
    }
  }

  form.addEventListener("submit", handleAnalysis);
  backButton.addEventListener("click", () => showView("hero"));
  downloadButton.addEventListener("click", handleDownload);
});
