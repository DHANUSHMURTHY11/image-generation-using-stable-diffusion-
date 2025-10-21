document.addEventListener("DOMContentLoaded", function () {
  let imageContainer = document.getElementById("generated-image");
  
  // Retrieve the stored image URL from local storage
  let imageURL = localStorage.getItem("generatedImageURL");

  if (imageURL) {
      imageContainer.src = imageURL;
      imageContainer.alt = "AI Generated Image";
  } else {
      document.body.innerHTML = "<h2>Error: No image found. Please generate an image first.</h2><a href='/generate'>Go back</a>";
  }
});
