<template>
  <div id="clock">
    <p class="date">{{ this.date }}</p>
    <p class="time">{{ time }}</p>
    <p class="text">Hello SSAFY!</p>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      time: '',
      date: '',
      interval: 0
    }
  },
  methods: {
    updateTime: function() {
      var week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
      var cd = new Date()
      this.time = this.zeroPadding(cd.getHours(), 2) + ':' + this.zeroPadding(cd.getMinutes(), 2) + ':' + this.zeroPadding(cd.getSeconds(), 2)
      this.date = this.zeroPadding(cd.getFullYear(), 4) + '-' + this.zeroPadding(cd.getMonth()+1, 2) + '-' + this.zeroPadding(cd.getDate(), 2) + ' ' + week[cd.getDay()]
      
      setTimeout(this.updateTime, 1000);
    },
    zeroPadding: function(num, digit) {
      var zero = '';
      for(var i = 0; i < digit; i++) {
          zero += '0';
      }
      return (zero + num).slice(-digit);
    },
  },
  mounted: function() {
    this.updateTime()
  },
}
</script>

<style lang="scss">

  p {
      margin: 0;
      padding: 0;
  }
  #clock {
      font-family: 'Share Tech Mono', monospace;
      color: #ffffff;
      text-align: center;
      position: relative;
      color: #daf6ff;
      text-shadow: 0 0 20px rgba(10, 175, 230, 1),  0 0 20px rgba(10, 175, 230, 0);
      .time {
          letter-spacing: 0.05em;
          font-size: 150px;
          padding: 5px 0;
      }
      .date {
          letter-spacing: 0.1em;
          font-size: 50px;
      }
      .text {
          letter-spacing: 0.1em;
          font-size: 50px;
          padding: 20px 0 0;
      }
  }
</style>