<template>
    <!-- <p>asdfs</p> -->
    <ds-calendar-app :calendar="calendar"></ds-calendar-app>
</template>
<style>
.v-toolbar--fixed{
  position: relative !important;
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
