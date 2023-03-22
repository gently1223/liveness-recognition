<template>
  <v-container  :class="{
        'container pa-4 my-12': $vuetify.breakpoint.smAndDown,
        'container pa-10 my-12': $vuetify.breakpoint.mdAndUp,
      }">
    <!-- avatar -->
    <v-row class="justify-center">
      <v-avatar size="150px">
        <img src="../assets/img/avatar.jpg" />
      </v-avatar>
    </v-row>
    <!-- name -->
    <v-row class="justify-center pb-5">
      <span class="title text-secondary py-2 font-weight-bold">{{ name }}</span>
    </v-row>
    <v-row>
        <v-col cols="12" lg="6">
            <p class="title text-secondary py-2 font-weight-bold">TITLE</p>
            <div class="row justify-space-between mt-5 mb-5">
                <v-btn color="primary" @click="showModal = true">
                    Select Exercise
                </v-btn>
                <v-btn
                    class="mx-2"
                    dark
                    color="teal"
                    @click="showSettingsModal = true"
                >
                <v-icon dark>
                    mdi-format-list-bulleted-square
                </v-icon>
                </v-btn>
            </div>
            <div class="imageZoom">
                <vue-hover-zoom
                    showWhenImageLoaded="true"
                    :imageUrl="getImgUrl()"
                >
                </vue-hover-zoom>
            </div>
            
        </v-col>
        <v-col cols="12" lg="6">
            <p class="title text-secondary py-2 font-weight-bold">EXERCISE</p>
            <v-select
                :items="uptodown_items"
                label="Up to Down"
                dense
                solo
            ></v-select>
            <v-img
              :aspect-ratio="16/9"
              :height="500"
              :src="getImgUrl()"
            ></v-img>
            <p class="title text-secondary py-2 font-weight-bold">EXERCISE</p>
            <v-img
              :aspect-ratio="16/9"
              :height="200"
              :src="getAnswerUrl()">
            </v-img>
            <v-row class="mt-5 justify-center">
                <v-btn
                  rounded
                  color="primary"
                  dark
                >
                  Check Answer
                </v-btn>
                &nbsp;&nbsp;&nbsp;              
              <p class="py-2 font-weight-bold">Preview: </p>&nbsp;<p class="py-2 font-weight-bold">Correct</p>
            </v-row>
            <v-row class="mt-5 justify-space-between dialog">
                <v-col>
                <v-btn
                  class="ma-2"
                  outlined
                  color="indigo"
                  width="120"
                >
                  Correct
                </v-btn>
                <p>{{level[0]}}</p>
                </v-col>
                <v-col>
                <v-btn
                  class="ma-2"
                  outlined
                  color="indigo"
                  width="120"
                >
                  Easy
                </v-btn>
                <p>{{level[1]}}</p>
                </v-col>
                <v-col>
                <v-btn
                  class="ma-2"
                  outlined
                  color="indigo"
                  width="120"
                >
                  Mistake
                </v-btn>
                <p>{{level[2]}}</p>
                </v-col>
                <v-col>
                <v-btn
                  class="ma-2"
                  outlined
                  color="indigo"
                  width="120"
                >
                  Difficult
                </v-btn>
                <p>{{level[3]}}</p>
                </v-col>
                <v-col>
                <v-btn
                  class="ma-2"
                  outlined
                  color="indigo"
                  width="120"
                >
                  Skip
                </v-btn>
                </v-col>
            </v-row>
            <v-row class="mt-10">
              <v-col>
                <v-btn
                  rounded
                  color="primary"
                  dark
                  width="150"
                >
                  Restart
                </v-btn>
              </v-col>
              <v-col>
                <v-select
                  :items="items"
                  :style="{width: '100px'}"
                  label="In Order"
                  dense
                  outlined
                  width="150"
                ></v-select>
              </v-col>
              <v-col>
                <v-btn
                    rounded
                    width="150"
                >
                  Close
                </v-btn>
              </v-col>
              <v-col>
                <v-btn
                  rounded
                  color="primary"
                  darkwidth="150"
                >
                  Check Progress
                </v-btn>
              </v-col>
            </v-row>
        </v-col>
    </v-row>

    <!-- List Modal -->
    <transition name="fade" appear>
        <div class="modal-overlay"
            v-if="showModal"
            @click="showModal = false">
        </div>
    </transition>
    <transition name="pop" appear>
        <div class="modal"
            role="dialog"
            v-if="showModal"
            >
            <h1>Vue Transitions</h1>
            <v-list shaped dense min-height="240">
                <v-subheader>SUBJECTS</v-subheader>
                <v-list-item-group
                    v-model="selectedItem"
                    color="primary">
                        <v-list-item
                            v-for="(item, i) in items"
                            :key="i">
                            <v-list-item-icon>
                              <v-icon v-text="item.icon"></v-icon>
                            </v-list-item-icon>
                            <v-list-item-content>
                              <v-list-item-title v-text="item.text"></v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                </v-list-item-group>
            </v-list>
            <v-file-input
                v-model="files"
                color="deep-purple accent-4"
                counter
                label="File input"
                multiple
                placeholder="Select your files"
                prepend-icon="mdi-paperclip"
                outlined
                :show-size="1000"
            >
                <template v-slot:selection="{ index, text }">
                    <v-chip
                      v-if="index < 2"
                      color="deep-purple accent-4"
                      dark
                      label
                      small
                    >
                      {{ text }}
                    </v-chip>

                    <span
                      v-else-if="index === 2"
                      class="text-overline grey--text text--darken-3 mx-2"
                    >
                      +{{ files.length - 2 }} File(s)
                    </span>
                </template>
            </v-file-input>
            <v-btn color="primary" @click="onClickOk">OK</v-btn>&nbsp;&nbsp;&nbsp;
            <v-btn outlined color="indigo" @click="showModal = false">CANCEL</v-btn>
        </div>
    </transition>
    <!-- Treeview Modal -->
    <transition name="fade" appear>
        <div class="modal-overlay"
            v-if="showTreeviewModal"
            @click="showTreeviewModal = false"></div>
    </transition>
    <transition name="pop" appear>
        <div class="modal"
              role="dialog"
              v-if="showTreeviewModal"
              >
            <h1>Vue Transitions</h1>
            <v-treeview
              selectable
              :items="rows"
              @update:active="onOpen"
              @input="onSelected"
            ></v-treeview>
            <v-btn color="primary" @click="onTreeviewOk">OK</v-btn>
        </div>
    </transition>
    <!-- Setting Modal -->
    <transition name="fade" appear>
      <div class="modal-overlay"
          v-if="showSettingsModal"
          @click="showSettingsModal = false"></div>
    </transition>
    <transition name="pop" appear>
      <div class="modal faq-body"
            role="dialog"
            v-if="showSettingsModal"
            >
          <h3>Waiting period for looking back</h3>
          <v-row>
              <v-col cols="4" class=" text-left">Correct(not difficult)</v-col>
              <v-col cols="4"><vue-numeric-input v-model="not_difficult_value" :min="1" :max="30" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="4">
                  <v-combobox
                    v-model="not_difficult_value_combo"
                    :items="not_difficult_value_items"
                    solo dense
                  ></v-combobox>
              </v-col>
          </v-row>
          <v-row>
              <v-col cols="4" class=" text-left">Correct(easy)</v-col>
              <v-col cols="4"><vue-numeric-input v-model="easy_value" :min="1" :max="30" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="4">
                  <v-combobox
                    v-model="easy_value_combo"
                    :items="easy_value_items"
                    solo dense
                  ></v-combobox>
              </v-col>
          </v-row>
          <v-row>
              <v-col cols="4" class=" text-left">Wrong(mistake)</v-col>
              <v-col cols="4"><vue-numeric-input v-model="mistake_value" :min="1" :max="30" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="4">
                  <v-combobox
                    v-model="mistake_value_combo"
                    :items="mistake_value_items"
                    solo dense
                  ></v-combobox>
              </v-col>
          </v-row>
          <v-row>
              <v-col cols="4" class=" text-left">Wrong(difficult)</v-col>
              <v-col cols="4"><vue-numeric-input v-model="difficult_value" :min="1" :max="30" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="4">
                  <v-combobox
                    v-model="difficult_value_combo"
                    :items="difficult_value_items"
                    solo dense
                  ></v-combobox>
              </v-col>
          </v-row>
          <h3>Planning</h3>
          <v-row class="mb-4">
              <v-col cols="4" class=" text-left">Number of exercises to do </v-col>
              <v-col cols="4" class=" text-left"><vue-numeric-input v-model="number_exercises_value" :min="1" :max="30" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
          </v-row>
          <v-row class="mb-4">
              <v-col cols="4" class=" text-left">Day of exercise </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="mon"
                label="Mon"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="tue"
                label="Tue"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="wen"
                label="Wen"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="thu"
                label="Thu"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="fri"
                label="Fri"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="sat"
                label="Sat"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="sun"
                label="Sun"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
          </v-row>
          <h3>Reward</h3>
          <v-row class="mb-4">
              <v-col cols="6">points </v-col>
              <v-col cols="3"><vue-numeric-input v-model="points_value" :min="1" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
          </v-row>
          <v-btn color="primary" @click="onSettingsOk">OK</v-btn>&nbsp;&nbsp;&nbsp;
          <v-btn outlined color="indigo" @click="showSettingsModal = false">CANCEL</v-btn>
      </div>
    </transition>
  </v-container>
</template>

<script>
import VueNumericInput from 'vue-numeric-input'
import VueHoverZoom from 'vue-hover-zoom'

export default {
  components: {
      VueNumericInput,
      VueHoverZoom
  },
  data: () => ({
      // imgURL: 'https://picsum.photos/id/1005/600/200',
      imgURL: 'OM1-1.jpeg',
      imgAnswerURL: 'OM!-1.jpeg',
      showModal: false,
      showTreeviewModal: false,
      showSettingsModal: false,
      selectedItem: 0,
      not_difficult_value: 1,
      easy_value: 1,
      mistake_value: 1,
      difficult_value: 1,
      number_exercises_value: 1,
      uptodown_items: [
          'History',
      ],
      level: ["1 days" ,"4 weeks","4 hours","1 hours"],
      not_difficult_value_combo: ['Vuetify'],
      not_difficult_value_items: [
          'Programming',
          'Design',
          'Vue',
          'Vuetify',
        ],
      easy_value_combo: ['Design'],
      easy_value_items: [
          'Programming',
          'Design',
          'Vue',
          'Vuetify',
        ],
      mistake_value_combo: ['Vue'],
      mistake_value_items: [
          'Programming',
          'Design',
          'Vue',
          'Vuetify',
        ],
      difficult_value_combo: ['Vuetify'],
      difficult_value_items: [
          'Programming',
          'Design',
          'Vue',
          'Vuetify',
        ],
      points_value: 34,
      mon: false,
      tue: false,
      wen: false, 
      thu: false,
      fri: false,
      sat: false,
      sun: false,
      items: [
        { text: 'History', icon: 'mdi-clock' },
        { text: 'Audience', icon: 'mdi-account' },
        { text: 'Conversions', icon: 'mdi-flag' },
      ],
      files: [],
      rows: [
    {
      "id": 1,
      "name": "第１部　歴史のとらえ方と調べ方",
      "endPage": 1,
      "children": [
        {"id":2,  "name": "第１節　歴史の流れと時代区分" },
        {"id":3,  "name": "第２節　歴史の調べ方・まとめ方・発表のしかた" }
      ]
    },
    {
      "id": 4,
      "name": "第２部　歴史の大きな流れと時代の移り代わり",
      "children": [
        {
          "id": 5,

          "name": "第１章　古代　古代国家の成立と東アジア",
          "children": [
                {"id": 6, "name": "第１節　人類の登場から文明の発生へ" },
                {"id": 7,  "name": "第２節　東アジアの中の日本 "}
          ]
        },
        {
          "id": 8,
          "name": "第２章　中世　武家政権の成長と東アジア",
          "children": [
            {
              "id": 9,
              "name": "第１節　武士の世の始まり"
            }
          ]
        }
      ]
    }
],
  }),
  computed: {
    formData: {
      get: function () {
        return this.$store.getters["authPageModule/getFormData"];
      },
    },
    name() {
      if (!this.formData.firstName || !this.formData.lastName) return "Anas KASMI";
      else return this.formData.firstName + " " + this.formData.lastName;
    },
  },
  methods: {
    onOpen(e) {
      if (!this.__initial) {
        this.__initial = true
        return
      }
    },
    onSelected(e) {
      console.log('checkbox clicked', e)
    },
    onClickOk() {
        this.showModal = false;
        this.showTreeviewModal = true;
    },
    getImgUrl() {
      var images = require.context('../assets/img/', false, /\.jpeg$/)
      return images('./' + this.imgURL)
    },
    getImgAnswerUrl() {
        var images = require.context('../assets/img/', false, /\.jpeg$/)
      return images('./' + this.imgAnswerURL)
    },
    onTreeviewOk() {
      this.showTreeviewModal = false;
      this.axios
        .get("https://jsonplaceholder.typicode.com/todos/1")
        .then((response) => {
          this.$swal({
            title: "Updated",
            text: "Your Subject was updated successfully",
            icon: "success",
            confirmButtonText: "Done",
          });
        })
        .catch((error) => {
          this.$swal({
            title: "Oops, Something went wrong ! ",
            text: error.message,
            icon: "warning",
          });
        });
    },
    onSettingsOk() {
        //fake post request
      this.showSettingsModal = false;
      this.axios
        .get("https://jsonplaceholder.typicode.com/todos/1")
        .then((response) => {
          this.$swal({
            title: "Updated",
            text: "The Setting was updated successfully",
            icon: "success",
            confirmButtonText: "Done",
          });
        })
        .catch((error) => {
          this.$swal({
            title: "Oops, Something went wrong ! ",
            text: error.message,
            icon: "warning",
          });
        });
    },
    backToPreviousPage() {
      this.$router.back();
    },
    updateInfo() {
      //fake post request
      this.axios
        .get("https://jsonplaceholder.typicode.com/todos/1")
        .then((response) => {
          this.$swal({
            title: "Updated",
            text: "Your profile was updated successfully",
            icon: "success",
            confirmButtonText: "Done",
          });
        })
        .catch((error) => {
          this.$swal({
            title: "Oops, Something went wrong ! ",
            text: error.message,
            icon: "warning",
          });
        });
    },
  },
};
</script>

<style>
#parent { white-space: nowrap; }
.child { display: inline-block; }
.zoom {
  transition: transfrom .2s;
}
.zoom:hover {
  transform: scale(1.5);
}
.hover-zoom-image {
  width: 100%!important;
}
.dialog {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
}
.dialog:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
</style>