
<template>
<body class="text-center body">
  <div id="calendar">
    <div class="header">
      <button v-on:click="prevMonth()">Hi</button>
      {{moment(currentMonth+1,'MM').format('MMMM') }} {{currentYear}}
      <button
        v-on:click="nextMonth()"
      >></button>
    </div>
    <div v-for="(week, k) in calendar" class="week" :key="k">
      <div
        v-for="(day, i) in week.days"
        v-on:click="selectDay(day)"
        class="day"
        :key="i"
        v-bind:class="[{in : isSameMonth(day.date)}, 
                             {active : day.date == activeDay}]"
      >
        <div class="day-name">{{moment(day.date).format('ddd')}}</div>
        <div class="day-number">{{moment(day.date).format('DD')}}</div>
        <div class="day-event">
          <div class="active-event" v-if="day.event.length"></div>
        </div>
      </div>
    </div>

    <div class="seleted-day">{{daySelected}}</div>
  </div>
</body>
</template>

<style>
#calendar {
  width: 420px;
  margin-left: 30px;
  height: 570px;
  margin-top: 50px;

  .header {
    display: flex;
    justify-content: space-between;
    height: 30px;
    text-transform: uppercase;
  }

  .week {
    display: grid;
    grid-template-columns: auto auto auto auto auto auto auto;
    justify-items: center;
    align-items: center;
    .day {
      padding: 10px;
      padding-bottom: 8px;
      width: 40px;
      border-radius: 14px;
      transition: all 0.3s ease-in-out;

      &:hover {
        cursor: pointer;
      }
      &.active {
        box-shadow: 0px 0px 15px rgba(210, 210, 210, 0.5);
        .day-number {
          color: #31b3ab;
        }
      }
    }
  }
}

.day {
  text-align: center;
  &:not(.in) {
    color: rgba(52, 52, 52, 0.5);
  }

  .day-name {
    font-size: 0.5rem;
    text-transform: uppercase;
    margin-bottom: 5px;
    color: rgba(52, 52, 52, 0.5);
    letter-spacing: 0.7px;
  }
  .day-number {
    font-size: 1.5rem;
    letter-spacing: 1.5px;
  }
  .day-event {
    min-heigth: 0.5rem;
    position: relative;
    margin-bottom: 0.5rem;

    .active-event {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 0.5rem;
      height: 0.5rem;
      background-color: #ffc200;
    }
  }
}
</style>

<script>
export default {
  name: "Calendar",
  data() {
    return {
      startWeek: moment,
      activeDay: "",
      endWeek: moment,
      calendar: [],
      today: moment(),
      currentMonth: "",
      currentYear: "",
      daySelected: ""
    };
  },
  methods: {
    setMounthWeek: function() {
      this.startWeek = this.today
        .clone()
        .startOf("month")
        .clone()
        .week();
      this.endWeek = this.today
        .clone()
        .endOf("month")
        .clone()
        .week();

      if (this.today.month() === 11) {
        this.endWeek = 53;
      }
      this.calendar = [];
      for (var week = this.startWeek; week < this.endWeek + 1; week++) {
        console.log(week);
        this.calendar.push({
          week: week,
          days: this.getDay(week)
        });
      }
    },
    getDay: function(week) {
      return (days = Array(7)
        .fill(0)
        .map((n, i) => {
          let day = this.today
            .clone()
            .week(week)
            .startOf("week")
            .clone()
            .add(n + i, "day")
            .clone();
          let event = this.getDayEvent(day);
          return { date: day, event: event };
        }));
    },
    getDayEvent: function(day) {
      return events.filter(ev => {
        if (day.isSame(moment(new Date(ev.date)))) {
          return ev.event;
        } else {
          return "";
        }
      });
    },
    isSameMonth: function(day) {
      return day.month() === this.currentMonth;
    },
    nextMonth() {
      this.today.add(1, "month");
      this.setMonth();
      this.setYear();
      this.setMounthWeek();
    },
    prevMonth() {
      this.today.subtract(1, "month");
      this.setMonth();
      this.setYear();
      this.setMounthWeek();
    },
    setMonth: function() {
      this.currentMonth = this.today.month();
    },
    setYear: function() {
      this.currentYear = this.today.year();
    },
    selectDay: function(day) {
      this.activeDay = day.date;
      this.daySelected = day;
    }
  },
  mounted: function() {
    let recaptchaScript = document.createElement('script')
    recaptchaScript.async = true
    recaptchaScript.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment-with-locales.min.js')
    
    document.head.appendChild(recaptchaScript)
    this.setMonth();
    this.setYear();
    this.setMounthWeek();
    // console.log(this.calendar)
  }
};

// moment.locale('en')
// const events = [{
//   date: '02-10-2019',
//   event: 'coucou les ptits loups'
// },{
//   date: '03-16-2019',
//   event: 'Boom Party'
// },
//                ]
</script>