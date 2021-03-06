<template>
  <div class="tag-container">
    <div class="card">
      <div class="head">
        <h3>Eigenschaften bearbeiten</h3>
        <p>{{ value.length }} Eigenschaften für das Team ausgewählt</p>
      </div>

      <div class="taglist">
        <tag
          class="tag"
          v-for="skill in tagsWithSelection"
          :key="skill.id"
          :name="skill.name"
          @input="toggleTag(skill.id)"
          clickable="true"
          :selected="skill.selected"
        />
      </div>

      <div class="button">
        <button class="primary" @click.prevent="closeDialog">Schließen</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {
  Inject,
  Vue,
  Component,
  Prop,
  State,
  Provide,
  Emit,
  Watch
} from "nuxt-property-decorator";

import tag from "./skill.vue";
import { remove, find } from "lodash";

type KeyValuePair = {
  id: string;
  name: string;
};

@Component({
  components: { tag }
})
export default class extends Vue {
  @Prop({ type: Array, required: true, default: () => [] })
  skills!: KeyValuePair[];

  @Prop({ type: Array, required: true }) value!: string[];

  toggleTag(id: string) {
    if (!find(this.value, v => v == id)) {
      this.value.push(id);
    } else {

      // we must keep the array instance
      for (var i = 0; i < this.value.length; i++) {
        if (this.value[i] == id) {
          this.value.splice(i, 1);
        }
      }
    }

    console.debug("Toggle", id, "result", this.value);
    this.update();
  }

  @Emit("input")
  update() {
    return this.value;
  }

  @Emit("close-dialog")
  closeDialog() {
    console.debug("close dialog");
  }

  get tagsWithSelection() {
    return this.skills.map(s => ({
      ...s,
      selected: this.value.find(v => v == s.id)
    }));
  }
}
</script>

<style lang="scss" scoped>
@import "assets/colors";
@import "@/assets/scales";

.taglist {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;

  .tag {
    margin-right: 12px;
    margin-bottom: 22px;
  }

  margin-top: 22px;
}

.tag-container {
  position: fixed;
  width: 100vw;
  height: 100vh;

  top: 0;
  left: 0;

  background: #00000080;
  z-index: 3;

  .card {
    max-width: 1000px;
    max-height: 700px;
    background: $background;
    position: relative;

    top: calc(50% - 40px);
    left: calc(50% - 40px);
    transform: translate(-50%, -50%);

    border-radius: 10px;
    margin: 40px;
    padding: 20px;
    overflow-y: scroll;

    display: flex;
    flex-direction: column;

    .head {
      display: flex;
      flex-direction: column;

      h3 {
        width: 100%;
      }
    }

    .button {
      padding-top: 10px;
      display: flex;
      flex-direction: row;
      justify-content: center;
    }
  }
}
</style>
