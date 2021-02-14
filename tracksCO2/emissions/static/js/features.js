document.getElementById("products").addEventListener("click", function (e) {
    if (e.target.tagName === "A") {
        e.preventDefault();
        var row = e.target.parentNode.parentNode;
        while ((row = nextTr(row)) && !/\bparent\b/.test(row.className))
            toggle_it(row);
    }
});

function nextTr(row) {
    while ((row = row.nextSibling) && row.nodeType != 1) ;
    return row;
}

function toggle_it(item) {
    if (/\bopen\b/.test(item.className))
        item.className = item.className.replace(/\bopen\b/, " ");
    else
        item.className += " open";
}


// {#    var varData = [];#}
// {#    var actuals = JSON.parse('{{ all_data | safe }}');#}
// {#console.log(actuals[0].fields.creation_timestamp);#}
// {#    var result = () => {#}
// {#        for (let x = 0; x < actuals.length; x++) {#}
// {#            let pureData = actuals[x].fields;#}
// {#            varData.push(pureData)#}
// {#        }#}
// {#    };#}
// {#    result();#}
// {#console.log(varData);#}
// {#    var result2 = () => {#}
// {#        for (let x = 0; x < varData.length; x++){#}
// {#            console.log(varData[x].start_city);#}
// {#            document.getElementById("sthsth").innerHTML += (varData[x].start_city+"<br />");#}
// {#        }#}
// {#    };#}
// {#    result2();#}
// {#let dictionary = Object.assign({}, ...varData.map((x) => ({#}
// {#    [x.start_time]: x.start_time,#}
// {#})));#}
// {##}