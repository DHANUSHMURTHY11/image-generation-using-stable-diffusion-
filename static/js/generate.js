document.getElementById("generate-form").addEventListener("submit", async function (event) {
    event.preventDefault();
    
    let prompt = document.getElementById("prompt").value;
    let progressBar = document.getElementById("progress-bar");
    let spinner = document.getElementById("spinner");
    let progressStatus = document.getElementById("progress-status");
    let resultDiv = document.getElementById("result");
    let generatedImage = document.getElementById("generated-image");
    
    // Hide previous results and show loading spinner
    resultDiv.classList.add("hidden");
    progressBar.classList.remove("hidden");
    spinner.classList.add("active");
    progressStatus.innerText = "Generating Image... Please Wait";
    progressStatus.style.color = "#00d4ff";
    
    try {
        let response = await fetch("/generate", {
            method: "POST",
            body: new URLSearchParams({ prompt: prompt }),
            headers: { "Content-Type": "application/x-www-form-urlencoded" }
        });
        
        let data = await response.json();
        
        if (data.file_url) {
            // Start polling to check if image exists
            checkImageExists(data.file_url, spinner, progressBar, progressStatus, resultDiv, generatedImage);
        } else {
            // Error: no file URL returned
            spinner.classList.remove("active");
            progressStatus.innerText = "Error: Unable to generate image. Try again.";
            progressStatus.style.color = "#ff0055";
        }
    } catch (error) {
        console.error("Error fetching image:", error);
        spinner.classList.remove("active");
        progressStatus.innerText = "Failed to generate image. Please try again.";
        progressStatus.style.color = "#ff0055";
    }
});

/**
 * Polls the server to check if the generated image exists
 * Retries every 2 seconds until the image is available
 */
function checkImageExists(imageUrl, spinner, progressBar, progressStatus, resultDiv, generatedImage) {
    const img = new Image();
    
    img.onload = function() {
        // Image exists and loaded successfully
        spinner.classList.remove("active");
        progressBar.classList.add("hidden");
        
        // Display the generated image with fade-in animation
        generatedImage.src = imageUrl;
        generatedImage.alt = "Generated Image";
        resultDiv.classList.remove("hidden");
    };
    
    img.onerror = function() {
        // Image doesn't exist yet, retry after 2 seconds
        setTimeout(() => {
            checkImageExists(imageUrl, spinner, progressBar, progressStatus, resultDiv, generatedImage);
        }, 2000);
    };
    
    // Add timestamp to prevent browser caching
    img.src = imageUrl + '?t=' + new Date().getTime();
}
