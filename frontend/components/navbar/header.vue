<template>
  <div class="item-header">
    <slot />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "nuxt-property-decorator";

@Component
export default class extends Vue {
}
</script>

<style scoped lang="scss">
@import "@/assets/colors";
@import "@/assets/scales";

.item-header {
  font-size: $h3FontSize;
  color: $headercolor;
  font-weight: bold;

  padding-left: 24px;
  padding-right: 15px;

  padding-top: 24px;
  padding-bottom: 24px;

  width: 100%;
  background-color: $background;
}
</style>
