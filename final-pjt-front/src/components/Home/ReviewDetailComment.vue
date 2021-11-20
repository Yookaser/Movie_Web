<template>
  <li>
    <span>{{ comment.commentusername }}: {{ comment.content }}</span>
  </li>
</template>

<script>

export default {
  props: {
    comment: {
      type: Object
    }
  }
}
</script>

<style>

</style>