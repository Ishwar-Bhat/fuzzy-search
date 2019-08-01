function initSearch(){
    // Add event-listner for value change
    document.getElementById("searchInput").addEventListener("input", function(e) {
        let inpValue = this.value.toUpperCase();
        if(inpValue === null || inpValue === undefined || inpValue === ""){
            // On blank value, remove all suggestions
            clearHelpList();
        }
        else{
            fetch("/search?word=" + this.value)
            .then( res => {
                return res.json();
            })
            .then( data => {
                // generate new suggestion list
                generateList(inpValue, data);
            })
            .catch( error => {
                console.log(error);
            });
        }
    });

    function generateList(inpValue, wordList) {
        var helpList;
        // Clear all suggestion and build new
        clearHelpList();
        helpList = document.createElement("DIV");
        helpList.setAttribute("id", "autocomplete-list");
        helpList.setAttribute("class", "autocomplete-items");
        document.getElementById("data-container").appendChild(helpList);

        wordList.forEach((word, index) => {
            let ele = document.createElement("DIV");
            if (inpValue === word.toUpperCase()){
                ele.innerHTML = "<strong>" + word + "</strong>";
            }
            else{
                let subStrInd = word.toUpperCase().indexOf(inpValue);
                if(subStrInd === 0) {
                    ele.innerHTML = "<strong>" + word.substr(0, inpValue.length) + "</strong>";
                    ele.innerHTML += word.substr(inpValue.length, word.length);
                }
                else {
                    ele.innerHTML = word.substr(0, subStrInd);
                    ele.innerHTML += "<strong>" + word.substr(subStrInd, inpValue.length); + "</strong>";
                    if(word.length > inpValue.length + subStrInd) {
                        ele.innerHTML += word.substr(inpValue.length + subStrInd, word.length);
                    }
                }
            }
            ele.addEventListener("click", (e) => {
                document.getElementById("searchInput").value = ele.textContent;
                clearHelpList();
            });
            helpList.appendChild(ele);
        });
    }

    function clearHelpList(){
        try {
            let helpListHolder = document.getElementById("autocomplete-list");
            helpListHolder.parentNode.removeChild(helpListHolder);
        }
        catch(error) {
        }
    }

    document.addEventListener("click", function (e) {
        clearHelpList();
    });
}