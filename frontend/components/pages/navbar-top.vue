<template>
  <div :height="'calc(100vh - ' + TOPHEIGHT + 'px)'" class="scroller">
    <slot />
    <div class="spacer" />
    <imprint class="imprint" :horizontal="true" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "nuxt-property-decorator";
import { Context } from "@nuxt/types";
import imprint from "@/components/imprint.vue";

@Component({ components: { imprint } })
export default class extends Vue {
  TOPHEIGHT = 148;
}
</script>

<style lang="scss" scoped>
@import "@/assets/scales";
@import "@/assets/colors";

.spacer {
  padding-bottom: $pageMarginBottom;
}

.scroller {
  overflow-y: scroll;
  -webkit-overflow-scrolling: touch;

  padding: $gridsize;
  padding-right: $pageMarginRight;

  flex: 1;
  align-items: unset;
  align-content: unset;
}

.imprint {
  padding-top: $pageMarginMin;
  margin-bottom: -$pageMarginMin;
  margin-left: -$pageMarginMin;
}

@media only screen and (max-width: $breakpoint_md) {
  .scroller {
    overflow: unset;
    width: 100vw;

    padding-left: $pageMarginMin;
    padding-right: $pageMarginMin;
  }


  // only need this when we want to do scroll detectio inside
  // .main {
  //   overflow-y: scroll;
  // }
}
</style>
