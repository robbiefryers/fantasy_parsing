var page = require("webpage").create(),
    url = "https://draftfantasyfootball.co.uk/league/k3viHLvuNpaYG6QFJ/headToHeadMatch/P3Aj6PYudQ7KoLEMW";



page.open(url, function (status) {
    if (status !== 'success') {
        console.log('Unable to load the address!');
        phantom.exit();
    } else {
        window.setTimeout(function () {
			  
			console.log(page.content);

            phantom.exit();
        }, 5000); // Change timeout as required to allow sufficient time 
    }
});

/*
function onPageReady() {
    var htmlContent = page.evaluate(function () {
        return document.documentElement.outerHTML;
    });

    console.log(htmlContent);

    phantom.exit();
}

page.open(url, function (status) {
    function checkReadyState() {
        setTimeout(function () {
            var readyState = page.evaluate(function () {
                return document.readyState;
            });

            if ("complete" === readyState) {
                onPageReady();
            } else {
                checkReadyState();
            }
        });
    }

    checkReadyState();
});*/