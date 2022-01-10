var rows = document.querySelector(".row.end")
var parentNode = document.querySelector(".container")
console.log(rows)

const options ={
    threshold:0.5
}


function grabData(response){
    return response.json()
}

const sleep = ms => new Promise(
    resolve => setTimeout(resolve, ms));
function loadData(entries,observer){
    entries.forEach(function(entry){
        console.log(entry)
        console.log(entry.intersectionRatio)
        console.log("IN")
        if(entry.isIntersecting){
            console.log("INTER")
        }
        for(var i = 0;i < 1; i++){
            console.log("End of page");
            var div = document.createElement("div")
            div.classList.add("row")

            sleep(1000).then(()=>{
                fetch('https://jsonplaceholder.typicode.com/todos/1')
                .then(function(response){
                    return response.json()
                })
                .then(data=>{
                    var title =data['title']
                    div.innerHTML = title
                })
                parentNode.insertBefore(div,rows).focus()
            })
            
        }
    });
}
var intersectionObserver = new IntersectionObserver(loadData,options);
intersectionObserver.observe(rows)