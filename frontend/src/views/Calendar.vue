<template>
    <!-- <p>asdfs</p> -->
    <ds-calendar-app :calendar="calendar" fixed app></ds-calendar-app>
</template>
<style>
.v-toolbar--fixed{
  position: relative !important;
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
