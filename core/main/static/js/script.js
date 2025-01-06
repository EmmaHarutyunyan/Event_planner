document.addEventListener('DOMContentLoaded', function () {
    const dateInput = document.getElementById('date');
    const calendarPopup = document.getElementById('calendar-popup');
    const prevMonthBtn = document.getElementById('prev-month');
    const nextMonthBtn = document.getElementById('next-month');
    const calendarMonth = document.getElementById('calendar-month');
    const calendarGrid = document.querySelector('.calendar-grid');
    
    let currentDate = new Date(); 
    let selectedDate = null;

    function generateCalendar(year, month) {
        const firstDay = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();
        
        calendarGrid.innerHTML = '';
        
        for (let i = 0; i < firstDay; i++) {
            const emptyCell = document.createElement('div');
            calendarGrid.appendChild(emptyCell);
        }
        
        for (let i = 1; i <= daysInMonth; i++) {
            const dayCell = document.createElement('div');
            dayCell.classList.add('calendar-cell');
            dayCell.textContent = i;
            dayCell.addEventListener('click', () => selectDate(i));
            calendarGrid.appendChild(dayCell);
        }
        const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
        calendarMonth.textContent = `${months[month]} ${year}`;
    }

    function selectDate(day) {
        selectedDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), day);
        dateInput.value = `${selectedDate.getFullYear()}-${(selectedDate.getMonth() + 1).toString().padStart(2, '0')}-${selectedDate.getDate().toString().padStart(2, '0')}`;
        calendarPopup.style.display = 'none';
    }
    dateInput.addEventListener('click', () => {
        calendarPopup.style.display = 'block';
        generateCalendar(currentDate.getFullYear(), currentDate.getMonth());
    });

    document.addEventListener('click', (e) => {
        if (!calendarPopup.contains(e.target) && e.target !== dateInput) {
            calendarPopup.style.display = 'none';
        }
    });

    prevMonthBtn.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        generateCalendar(currentDate.getFullYear(), currentDate.getMonth());
    });

    nextMonthBtn.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        generateCalendar(currentDate.getFullYear(), currentDate.getMonth());
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const countDownDate = new Date("Jan 15, 2025 15:00:00").getTime();

    const x = setInterval(function () {
        const now = new Date().getTime();
        const distance = countDownDate - now;

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById("days").innerText = days.toString().padStart(2, '0');
        document.getElementById("hours").innerText = hours.toString().padStart(2, '0');
        document.getElementById("minutes").innerText = minutes.toString().padStart(2, '0');
        document.getElementById("seconds").innerText = seconds.toString().padStart(2, '0');

        if (distance < 0) {
            clearInterval(x);
            document.getElementById("timer").innerHTML = "EXPIRED";
        }
    }, 1000);
});

document.addEventListener('DOMContentLoaded', function () {
    flatpickr("#date", {
        dateFormat: "Y-m-d", 
        allowInput: true, 
        disableMobile: true, 
        onChange: function(selectedDates, dateStr, instance) {
            document.getElementById('date').value = dateStr;
        },
        theme: "material_red",
        onReady: function() {
            const calendar = document.querySelector('.flatpickr-calendar');
            const selectedDate = document.querySelector('.flatpickr-selected');
            if (selectedDate) {
                selectedDate.style.backgroundColor = "#e74c3c"; 
                selectedDate.style.color = "white"; 
            }
        }
    });
});



document.addEventListener("DOMContentLoaded", function () {
    const invitations = document.querySelectorAll('.invitation-container');

    invitations.forEach((invitation) => {
        invitation.addEventListener('click', () => {
            alert(`You clicked on a ${invitation.dataset.type} invitation!`);
        });
    });
});

