console.log("frontend running");
const baseUrl = "http://localhost:9828";
const RandImgBtn = document.getElementById("RandomIButton");

const featureForm = $("#featureForm");

const outputBox = $("#outputBox");

const txtLoader = document.getElementById("txtLoader");

RandImgBtn.addEventListener("click", e => {
  e.preventDefault();

  outputBox.html(`<div class="loader loader--style5 text-center" title="4">
        <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
          x="0px" y="0px" width="24px" height="30px" viewBox="0 0 24 30" style="enable-background:new 0 0 50 50;"
          xml:space="preserve">
          <rect x="0" y="0" width="4" height="10" fill="#333">
            <animateTransform attributeType="xml" attributeName="transform" type="translate" values="0 0; 0 20; 0 0"
              begin="0" dur="0.6s" repeatCount="indefinite" />
          </rect>
          <rect x="10" y="0" width="4" height="10" fill="#333">
            <animateTransform attributeType="xml" attributeName="transform" type="translate" values="0 0; 0 20; 0 0"
              begin="0.2s" dur="0.6s" repeatCount="indefinite" />
          </rect>
          <rect x="20" y="0" width="4" height="10" fill="#333">
            <animateTransform attributeType="xml" attributeName="transform" type="translate" values="0 0; 0 20; 0 0"
              begin="0.4s" dur="0.6s" repeatCount="indefinite" />
          </rect>
        </svg>
      </div>`);
  // $.ajax({
  // 	url: `${baseUrl}/random-image`,
  // 	headers: { "Access-Control-Allow-Origin": `${baseUrl}/random-image` },
  // 	type: "GET",
  // 	crossDomain: true,

  // 	success: function(fileName) {
  // 		if (fileName) {
  // 			outputBox.html(
  // 				`<img class="card-img-top random-image" src="${baseUrl}/dcgan/resultImg/${fileName}">`
  // 			);
  // 		}
  // 	},
  // 	error: function(xhr, status) {
  // 		alert("error");
  // 	}
  // });
  setTimeout(() => {
    outputBox.html(
      `<h2> The Compressed Video </h2>
			<video width="320" height="240" controls>
				<source src="../video-compression/gen_shit1.mp4" type="video/mp4" />
			</video>
			<h2> The Decompressed Video </h2>
			<video width="320" height="240" controls>
				<source src="../video-compression/gen_shit2.mp4" type="video/mp4" />
			</video>
			`
    );
  }, 10000);
});
