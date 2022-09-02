
$(document).ready(function(){
    $("#sld").datepicker({
        minDate: 0,
        maxDate: 3,
    });
});


// seat selectiion section
var busId
var busName
var busPrice
var busuniqueid
const container = document.querySelector('.select-container');
const seats = document.querySelectorAll('.seat-row .seat:not(.occupied)');
const count= document.getElementById('count');
const total = document.getElementById('total');
const price = document.getElementById('fare');
// const amountbtn = document.getElementById('book-btn');
// console.log(amountbtn.value);
// let ticketPrice = +price.value;
console.log(busPrice)
// let ticketPrice = busPrice
// console.log('ticketPrice',ticketPrice)
// const ticketPrice = ticketPrice;
// console.log(ticketPrice);
const selectedSeats = document.querySelectorAll('.seat-row .seat.selected');
// console.log('selectedSeats:',selectedSeats)



// update total and count
function updateSelectedCount(){
    const selectedSeats = document.querySelectorAll('.seat-row .seat.selected');
    const seatsIndex = [...selectedSeats].map(function(seat){
        return[...seats].indexOf(seat);
    });
    localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));
    // console.log(seatsIndex)

    const selectedSeatsCount = selectedSeats.length;
    console.log(selectedSeatsCount);
    count.innerText = selectedSeatsCount;
    total.innerText = selectedSeatsCount*ticketPrice;
    // myfunc(lol)
}

function myfunc(myvar){
    let ans = myvar.attributes.for.value;
    console.log('ans',ans)
    movieTitle = myvar.getAttribute('data-busName')
    console.log(movieTitle)
    let ans1= ans.split("#");
    var iterator = ans1.values();
    ticketPrice= iterator.next().value;
    updateSelectedCount();
}

const modalBtns = [...document.getElementsByClassName('modal-button')];
                                    // console.log(modalBtns)
const modalHeading = document.getElementById('heading');
const modalSeatMgmnt = document.getElementById('bussesSeat')
// console.log(modalHeading)



// modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
//     busId = modalBtn.getAttribute('data-busId');
//     busName = modalBtn.getAttribute('data-busName');
//     console.log ('seats',seats)
//     all_seats = modalBtn.querySelectorAll('.seat-row .seat')
//     console.log ('all_seats',all_seats)
//     const routeId = modalBtn.getAttribute('data-routeId');
//     const busSeat = modalBtn.getAttribute('data-busSeat');
//     const seatType = modalBtn.getAttribute('data-seatType');
//     busPrice= modalBtn.getAttribute('data-busPrice');
//     // console.log(busPrice)

//     localStorage.setItem('selectedBusIndex',busId);
//     localStorage.setItem('selectedBusPrice',busPrice);
//     modalHeading.innerHTML=`
//     <p class="text-center" id="heading"><b> Select ${busName} Seat</b></p>
//     `

// }))

// console.log(modalBtns.busName)



container.addEventListener('click',(e)=>{
    if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')){
        e.target.classList.toggle('selected')
    }
    updateSelectedCount();
})


// modal clear after closing()


// window.addEventListener('DOMContentLoaded', (event) => {
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', ()=>{
    $(document).ready(function() {
        $('#mymodal').on('hidden.bs.modal', function() {
            history.go(0);
        });
        });
    busId = modalBtn.getAttribute('data-busId');
    busName = modalBtn.getAttribute('data-busName');
    busuniqueid =modalBtn.getAttribute('data-busuniqueid');
    // console.log ('seats',seats)
    const all_seats = document.querySelectorAll('.seat-row .seat');
    console.log ('all_seats',all_seats)
    const routeId = modalBtn.getAttribute('data-routeId');
    const busSeat = modalBtn.getAttribute('data-busSeat');
    const seatType = modalBtn.getAttribute('data-seatType');
    busPrice= modalBtn.getAttribute('data-busPrice');
    // console.log(busPrice)

    localStorage.setItem('selectedBusIndex',busId);
    localStorage.setItem('selectedBusPrice',busPrice);
    localStorage.setItem('selectedBusName',busName);
    modalHeading.innerHTML=`
    <p class="text-center" id="heading"><b> Select ${busName} Seat</b></p>
    `   
    // modalSeatMgmnt.innerHTML=`
    // <div class="seat-row">

    // </div>
    // `
        // ---------------- backend stuffs---------------
    // body={busName: busName, busId: busId}
    // console.log(body)
    async function contactAPI(url,body){
        const response = await fetch(url,{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(body)
        })
        return response.json()
    }
    contactAPI("/occupied/",{busName, busId}).then(data=>{
        console.log(data)
        const occupied_seat = data["occupied_seats"]
        console.log('occupied_seat_backend',occupied_seat)
        const bus_title = data["bus"]
        const bus_iddata = data["busId"]
        console.log('bus_iddata:',bus_iddata)
        const seat_LocalStorage = localStorage.getItem('selectedSeats')?JSON.parse
        (localStorage.getItem('selectedSeats')):null
        const bus_index = localStorage.getItem('selectedBusIndex')
        const bus_name = localStorage.getItem('selectedBusName')

        const LS_bus = +bus_index
        console.log('LS_bus:',LS_bus)

        if (LS_bus == bus_iddata){
            console.log(true)
            if(occupied_seat != null && occupied_seat.length > 0){
                all_seats.forEach((seat, index)=>{
                    if(occupied_seat.indexOf(index)> -1){
                        seat.classList.add('occupied')
                        seat.classList.remove('selected')
                    }
                })
            }
            if (seat_LocalStorage != null){
                seat_LocalStorage.forEach((seat,index)=>{
                    if(occupied_seat.includes(seat)){
                        seat.localStorage.splice(index,1)
                        localStorage.setItem("selectedSeats",seat_LocalStorage)
                    }
                })
            }    
        }
        updateSelectedCount()
    })



}))
// });