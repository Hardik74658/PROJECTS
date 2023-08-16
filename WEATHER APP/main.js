
const fetchData = async (event) => {

    event.preventDefault();
    const location = document.getElementById('Location').value;
    const url = `https://yahoo-weather5.p.rapidapi.com/weather?location=${location}`;
    const res = await fetch(url, {
        method: "GET",
        headers: {
            'X-RapidAPI-Key': 'ed703d44c5mshf4e82943282a501p1fea69jsnf038142cf668',
            'X-RapidAPI-Host': 'yahoo-weather5.p.rapidapi.com'
        }
    })
    const finalres = await res.json();
    const temp = finalres.current_observation.condition.temperature;
    const atmosphere = finalres.current_observation.condition.text;
    const windSpeed = finalres.current_observation.wind.speed;
    const humidity = finalres.current_observation.atmosphere.humidity;
    // console.log(temp);
    const temp_celcius = parseInt((temp - 32) * (5 / 9));
    const d = new Date();
    const day = d.getDay();
    const date = d.toDateString();
    const hour = d.getHours();
    const day_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    // console.log(hour);
    weatherDetailsElement = document.querySelector('.weather-details');
    weatherDetailsElement.innerHTML = `<p>${day_array[day - 1]},${hour} Hour</p><p></p> <p> Date : </p><p>${date}</p> <p> Location : </p><p>${location}</p><p>Temperature : </p><p>${temp_celcius}°C</p><p> Atmosphere : </p><p>${atmosphere}</p><p> Wind Speed : </p><p>${windSpeed}kmph</p><p> Humidity : </p> <p>${humidity}</p>`;
    // console.log(finalres);
}