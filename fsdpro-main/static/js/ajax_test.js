document.addEventListener("DOMContentLoaded", function(){
    let form = document.getElementById("testForm");

    if(form){
        form.addEventListener("submit", function(e){
            e.preventDefault();

            fetch("", {
                method: "POST",
                body: new FormData(form),
                headers: {'X-Requested-With': 'XMLHttpRequest'}
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById("result").innerHTML = `
                    <h3>Score: ${data.score}</h3>
                    <h3>Final: ${data.final_score}</h3>

                    <div class="progress">
                        <div class="progress-bar" style="width:${data.final_score}%">
                            ${data.final_score}%
                        </div>
                    </div>

                    <canvas id="chart"></canvas>
                `;

                new Chart(document.getElementById("chart"), {
                    type: 'bar',
                    data: {
                        labels: ['Score','Final'],
                        datasets: [{ data: [data.score, data.final_score] }]
                    }
                });
            });
        });
    }
});