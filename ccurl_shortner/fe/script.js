// alert("testing")
console.log("Hello world")

var a = 12
console.log("Number = " + a)


async function postData(params) {
    let x = await fetch('http://localhost:8080/add', {
        method: 'POST',
        body: JSON.stringify({
            longUrl: 'https://www.example.com'
        }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
        },
      })
    let data = await x.json()
    console.log(data)
    return data
}

// postData()
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function wait() {
    console.log("Start waiting...");
    await sleep(30000);  // Waits for 3 seconds
    console.log("Waited 3 seconds!");
}
var buttonData = ""
function myFunction() {
	//  take fomr data and post it  
	alert("in my function")
	buttonData = document.getElementById("urlInput").value
	postData(buttonData)
	// wait()
	console.log(buttonData)
	alert("Done")
}

console.log(buttonData)