<template>
  <div class="page">
    <mq-layout mq="lg+">
      <sidebar :labels="labels" :selectedElement="selectedIndex" class="sidebar" />
    </mq-layout>
    <mq-layout :mq="['sm', 'md']">
      <topbar class="top" :hideMenu="true" />
    </mq-layout>
    <nuxt-child @selectelement="selectElement" class="screen-right" />
  </div>
</template>

<script lang="ts">
import { Component, Vue, Provide } from "nuxt-property-decorator";
import { ProvideReactive, Watch } from "vue-property-decorator";
import { Meta } from "@/components/decorator";

import sidebar from "@/components/pages/sidebar-register.vue";
import topbar from "@/components/pages/topbar.vue";
import auth from "@/components/auth/index.vue";

export enum RegistrationFlow {
  demand = "demand",
  supply = "supply"
}

export type Workflow = {
  type: RegistrationFlow;
  displayName: string;
};

@Component({
  components: {
    sidebar,
    auth,
    topbar,
  },
  layout: "registration"
})
export default class extends Vue {
  labels = ["Persönliche Daten", "Dein Unternehmen"];
  selectedIndex = 0;

  @ProvideReactive("workflow")
  providedWorfklow: Workflow | null = null;

  @Meta
  head() {
    return {
      title: this.providedWorfklow?.displayName,
      meta: [{ hid: "description", name: "description", content: "" }]
    };
  }

  selectElement(value: any) {
    console.debug("register", "selectElement", value);
    this.selectedIndex = value;
  }

  created() {
    console.debug("register", "created");

    this.providedWorfklow = {
      type: this.$route.params.flow as RegistrationFlow,
      displayName:
        this.$route.params.flow == "demand" ? "Ich suche" : "Ich biete"
    };

    this.labels.push(this.providedWorfklow.displayName);
  }
}
</script>

<style scoped lang="scss">
@import "@/assets/scales";

.page {
  display: flex;
  flex-direction: row;
}

.top {
  background-color: white;
}

.sidebar {
  display: flex;
  min-width: 330px;
  height: 100%;
}

.screen-right {
  display: flex;

  width: 100vw;
  min-height: 100vh;

  padding-top: 150px;
  padding-bottom: $gridsize;

  justify-content: center;
}

@media only screen and (max-width: $breakpoint_md) {
  .page {
    flex-direction: column;
  }

  .screen-right {
    padding-top: $gridsize;
    padding-bottom: $gridsize;

    flex-shrink: 0;
  }
}

@media only screen and (max-height: $breakpoint_sm) {
  .screen-right {
    padding-bottom: $gridsize;
    padding-top: $gridsize;
  }
}
</style>
