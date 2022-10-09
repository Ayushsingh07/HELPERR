let temperature=document.querySelector(".temp");
let icon=document.querySelector(".icon");
let content=document.querySelector(".summary");
let place=document.querySelector(".location");

document.addEventListener("DOMContentLoaded",()=>{
    document.querySelector("#form").addEventListener("submit",async(event)=>{
        event.preventDefault();
        const{target:{city}}=event;
        const api = "6d055e39ee237af35ca066f35474e9df";
        try{
            let response= await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city.value}&appid=${api}`)
            const data=await response.json();
            const kelvin = 273;
             //console.log(data);
            temperature.textContent=Math.floor(data.main.temp-kelvin)+"°C";
            content.textContent = data.weather[0].description;
            place.textContent = data.name + "," + data.sys.country;
          let icon1 = data.weather[0].icon;
          icon.innerHTML = 
              `<img src="img/${icon1}.svg" style= 'height:6rem'/>`;
           }
           catch (error){
               console.log("error");
           }
    })
})
