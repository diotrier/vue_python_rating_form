<template>
  <div>
    <h2>How would you rate your satisfaction with our product?</h2>
    <div class="stars">
      <span v-for="star in 5" :key="star" @click="rate(star)">
        {{ star <= rating ? '★' : '☆' }}
      </span>
      <div class="box">
        <div class="text_1">
          <h3>Very dissatified</h3>
        </div>
        <div class="text_2">
          <h3>Very satified</h3>
        </div>
      </div>
    </div>
    <button @click="submitRating">Submit</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      rating: 0
    }
  },
  methods: {
    rate(star) {
      this.rating = star
    },
    async submitRating() {
      try {
        await axios.post('http://localhost:5173/ratings/', { score: this.rating })
        alert('Rating submitted!')
      } catch (error) {
        console.error(error)
        alert('Failed to submit rating')
      }
    }
  }
}
</script>

<style>
.stars span {
  font-size: 2rem;
  cursor: pointer;
}
.box {
  display: flex;
  gap: 1rem;
}
</style>
