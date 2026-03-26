document.addEventListener('DOMContentLoaded', function () {
    const inputValor = document.getElementById('valor');
    const inputJuros = document.getElementById('juros');
    const inputPrazo = document.getElementById('prazo');

    const spanParcela = document.getElementById('resultado_parcela');
    const spanTotal = document.getElementById('resultado_total');
    const hiddenParcela = document.getElementById('parcela');
    const hiddenTotal = document.getElementById('valor_final');

    let grafico = null;

    function atualizarGrafico(principal, juros) {
        const ctx = document.getElementById('meuGrafico');
        if (!ctx) return;

        if (grafico) grafico.destroy();

        grafico = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Principal', 'Juros'],
                datasets: [{
                    data: [principal.toFixed(2), juros.toFixed(2)],
                    backgroundColor: ['#4c00ff', '#a855f7'],
                }]
            },
            options: {
                plugins: {
                    legend: {
                        labels: {
                            color: 'white'
                        }
                    }
                }
            }
        });
    }

    function calcular() {
        const P = parseFloat(inputValor.value) || 0;
        const i = (parseFloat(inputJuros.value) / 100) || 0;
        const n = parseInt(inputPrazo.value) || 0;

        if (P > 0 && i > 0 && n > 0) {
            const valorFinal = P * Math.pow((1 + i), n);
            const parcela = valorFinal / n;

            spanParcela.innerText = parcela.toFixed(2);
            spanTotal.innerText = valorFinal.toFixed(2);

            hiddenParcela.value = parcela.toFixed(2);
            hiddenTotal.value = valorFinal.toFixed(2);

            atualizarGrafico(P, valorFinal - P);
        }
    }

    if (inputValor) {
        inputValor.addEventListener('input', calcular);
        inputJuros.addEventListener('input', calcular);
        inputPrazo.addEventListener('input', calcular);
    }
});
