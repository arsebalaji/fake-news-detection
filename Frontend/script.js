const news = document.getElementById("news");

const analyze =
    document.getElementById("analyze");

const clear =
    document.getElementById("clear");

const count =
    document.getElementById("count");

const loading =
    document.getElementById("loading");

const result =
    document.getElementById("result");

const prediction =
    document.getElementById("prediction");

const score =
    document.getElementById("score");

const reason =
    document.getElementById("reasonText");


/* ==============================
   CHARACTER COUNTER
============================== */

news.addEventListener("input", () => {

    count.textContent =
        `${news.value.length} characters`;

});


/* ==============================
   CLEAR BUTTON
============================== */

clear.addEventListener("click", () => {

    news.value = "";

    count.textContent =
        "0 characters";

    result.classList.add("hidden");

});


/* ==============================
   DETECT NEWS
============================== */

analyze.addEventListener(
    "click",
    async () => {

        const text =
            news.value.trim();


        if (!text) {

            alert(
                "Please enter news first."
            );

            return;
        }


        loading.classList.remove(
            "hidden"
        );

        result.classList.add(
            "hidden"
        );


        analyze.disabled = true;


        try {

            const response =
                await fetch(
                    "/api/detect",
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            news: text

                        })

                    }
                );


            const data =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    data.error ||
                    "Detection failed"
                );

            }


            /* ==========================
               SHOW PREDICTION
            ========================== */

            if (
                data.prediction ===
                "FAKE"
            ) {

                prediction.innerHTML =
                    "❌ FAKE NEWS";

            } else {

                prediction.innerHTML =
                    "✅ REAL NEWS";

            }


            /* ==========================
               CONFIDENCE
            ========================== */

            score.textContent =
                `${data.confidence}%`;


            /* ==========================
               AI REASON
            ========================== */

            reason.textContent =
                data.reason;


            result.classList.remove(
                "hidden"
            );


        } catch (error) {

            console.error(error);

            alert(
                error.message
            );


        } finally {

            loading.classList.add(
                "hidden"
            );

            analyze.disabled = false;

        }

    }
);