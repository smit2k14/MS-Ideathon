console.log("frontend running");
const baseUrl = "http://localhost:9828";
const RandImgBtn = document.getElementById("RandomIButton");
const txtSummarize = document.getElementById("txtSummarize");

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

txtSummarize.addEventListener("click", e => {
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
  setTimeout(() => {
    outputBox.html(`<p>Fuhrmann, Rasputin was certainly close to Feodosiya and was godfather to her children, but "the records that have survived do not permit us to say more than that. His father, Yefim, was a peasant farmer and church elder who had been born in Pokrovskoye in 1842, and married Rasputin's mother, Anna Parshukova, in 1863. Local archival records suggest that he had a somewhat unruly youth – possibly involving drinking, small thefts, and disrespect for local authorities – but contain no evidence of his being charged with stealing horses, blasphemy, or bearing false witness, all major crimes that he was later rumored to have committed as a young man.

According to historian Douglas Smith, Rasputin's youth and early adulthood are "a black hole about which we know almost nothing", though the lack of reliable sources and information did not stop others from fabricating stories about his parents and his youth after Rasputin's rise to fame. Yefim also worked as a government courier, ferrying people and goods between Tobolsk and Tyumen The couple had seven other children, all of whom died in infancy and early childhood; there may have been a ninth child, Feodosiya</p>`);
  }, 7000);
});
