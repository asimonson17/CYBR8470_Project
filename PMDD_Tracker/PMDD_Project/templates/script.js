function escape(htmlStr) {
  return htmlStr.replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");        

}

console.log(escape("<script>alert('hi')</script>"));

const date = new Date();

const renderCalendar = () => {

    date.setDate(1);
    
    const monthDays = document.querySelector(".days");
    
//    const month = date.getMonth();
    
//get the last day of the month    
    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();

//get the last day of the previous month for backfilling calendar
    const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();

//get the first day of the month for an index
    const firstDayIndex = date.getDay();

//get the last day ofthe month for an index
    const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();

//use last day index to get the next days needed for the calendar
    const nextDays = 7 - lastDayIndex - 1;
    
    const months = [
        "January",
        "February",
        "March",
        "May",
        "April",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];
    
    //get current month and put it in the dates h1 variable
    document.querySelector('.date h1').innerHTML = months[date.getMonth()];
    
    //get the current date and place it in the dates p variable
    document.querySelector('.date p').innerHTML = new Date().toDateString();
    
    let days = "";
    
    //Calculate first days using prevlast day - firstday index and adding one
    for(let x = firstDayIndex; x > 0; x--) {
      days += `<div class="prev-date">${prevLastDay - x + 1} </div>`;  
    }
    
    for(let i = 1; i <= lastDay; i++) {
        if(i === new Date().getDate() && date.getMonth() === new Date().getMonth()) {
            days += `<div class=today">${i}</div>`;
        } else {
            days += `<div>${i}</div>`;
        }
    }
    
    for (let j = 1; j <= nextDays; j++) {
        days += `<div class="next-date">${j}</div>`; 
    }  monthDays.innerHTML = days;
}


//make the left arrow button on calendar go to previous month when clicked.
document.querySelector('.prev').addEventListener('click', () => {
    date.setMonth(date.getMonth() - 1);
    renderCalendar();
});

//make right arrow button on calendar go to next month when clicked.
document.querySelector('.next').addEventListener('click', () => {
    date.setMonth(date.getMonth() + 1);    
    renderCalendar();
});


renderCalendar();


const xValues = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]; 

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{ 
      data: [5,2,4,1,10,9,2,1,10,2,5,2,4,1,10,9,2,1,10,2,5,2,4,1,10,9,2,1,10,2,5],
      borderColor: "red",
      fill: false
    }, { 
      data: [4,6,4,8,3,7,4,8,3,7,4,6,4,8,3,7,4,8,3,7,4,6,4,8,3,7,4,8,3,7,6],
      borderColor: "green",
      fill: false
    }, { 
      data: [8,1,9,4,1,4,9,4,1,4,9,8,1,9,4,1,4,9,4,1,4,9,8,1,9,4,1,4,9,4,1,4,9],
      borderColor: "blue",
      fill: false
    }]
  },
  options: {
    legend: {display: false}
  }
});



//Chart