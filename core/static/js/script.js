// window.onload = function(){
//     var calander = document.getElementById("sld");
//     calander.nepaliDatePicker({
//         ndpYear: true,
//         ndpMonth: true,
//         ndpYearCount: 10,
//         disableDaysBefore: 0,
//         disableDaysAfter: 3

//     });
// };

$(document).ready(function(){
    $("#sld").datepicker({
        minDate: 0,
        maxDate: 3,
    });
});
// accordion
// const accordionTitles = document.querySelectorAll(".accordionTitle");
// accordionTitles.forEach((accordionTitle)=>{
//     accordionTitle.addEventListener("click", ()=>{
//         if(accordionTitle.classList.contains("is-open")){
//             accordionTitle.classList.remove("is-open");
//         }else{
//             const accordionTitlesWithIsOpen = document.querySelectorAll(".is-open");
//             accordionTitlesWithIsOpen.forEach((accordionTitleWithIsOpen)=>{
//                 accordionTitleWithIsOpen.classList.remove("is-open");
//             })
//             accordionTitle.classList.add("is-open");
//         }
//     })
// })

// seat selectiion section

const container = document.querySelector('.select-container');
const seats = document.querySelectorAll('.row .seat:not(.occupied)');
const count= document.getElementById('count');
const total = document.getElementById('total');
const price = document.getElementById('fare');
const amountbtn = document.getElementById('book-btn');
// console.log(amountbtn.value);
let ticketPrice = +price.textContent;
console.log(ticketPrice);

// update total and count
function updateSelectedCount(){
    const selectedSeats = document.querySelectorAll('.seat-row .seat.selected');
    const seatsIndex = [...selectedSeats].map(function(seat){
        return[...seats].indexOf(seat);
    })
    console.log(seatsIndex)
    const selectedSeatsCount = selectedSeats.length;
    console.log(selectedSeatsCount);
    count.innerText = selectedSeatsCount;
    total.innerText = selectedSeatsCount*ticketPrice;
}
// myfunc
function myfunc(myvar){
    let ans = myvar.attributes.for.value;
    let ans1= ans.split("#");
    var iterator = ans1.values();
    ticketPrice= iterator.next().value;
    updateSelectedCount();
}

const modalBtns = [...document.getElementsByClassName('modal-button')];
const modalHeading = document.getElementById('heading');

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
    const busId = modalBtn.getAttribute('data-busId');
    const busName = modalBtn.getAttribute('data-busName');
    const routeId = modalBtn.getAttribute('data-routeId');
    const busSeat = modalBtn.getAttribute('data-busSeat');
    const seatType = modalBtn.getAttribute('data-seatType');

    modalHeading.innerHTML=`
    <p class="text-center" id="heading"><b> Select ${busName} Seat</b></p>
    `
}))
// myfunc
// arr1=[];
// arr2=[];



// change ticket button value
// amountbtn.addEventListener('click', (e) =>{
//     ticketPrice = +e.target.value
//     console.log(ticketPrice);
//     updateSelectedCount();
// })

container.addEventListener('click',(e)=>{
    if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')){
        e.target.classList.toggle('selected')
    }
    updateSelectedCount();
})


// modal clear after closing()

$(document).ready(function() {
    $('#mymodal').on('hidden.bs.modal', function() {
      history.go(0);
    });
  });
