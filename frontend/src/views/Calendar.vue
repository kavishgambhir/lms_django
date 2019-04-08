<template>
    <!-- <p>asdfs</p> -->
    <ds-calendar-app :calendar="calendar" fixed app></ds-calendar-app>
</template>
<style>
body, html, #dayspan {
  font-family: Roboto, sans-serif;
  width: 100%;
  height: 100%;
}
.ds-calendar-app > .ds-app-calendar-toolbar{
    visibility: hidden!important;
}
</style>
<script>
import { Calendar } from 'dayspan';

export default {
  name: 'Calendar',
  data: () => ({
    calendar: Calendar.months()
  })
}
</script>
