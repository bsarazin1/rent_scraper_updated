axios({
  url: "https://vermont.craigslist.org/search/field/price?cl_url=https%3A%2F%2Fvermont.craigslist.org%2Fsearch%2Fone-bedroom-apartment%3Fsearch_distance%3D0%26postal%3D02760%26min_price%3D%26max_price%3D%26availabilityMode%3D0%26sale_date%3Dall%2Bdates",
  method: "get",
  mode: "no-cors",
  header: {
    "Content-Type": "application/json",
  },
  withCredentials: true,
  credentials: "same-origin",
}).then((res) => {
  console.log(res.data);
  console.log(res.status);
  console.log(res.statusText);
  console.log(res.headers);
  console.log(res.config);
});

const App = {
  data() {
    return {
      bedrooms: "",
      zip_codes: "",
      rooms: "",
      outputs: "",
      values: "",
      baseUrl:
        "https://vermont.craigslist.org/search/field/price?cl_url=https%3A%2F%2Fvermont.craigslist.org%2Fsearch%2F",
    };
  },

  created() {},

  methods: {
    getRooms() {
      console.log({ "this in getRooms": this });
      axios({
        url:
          this.baseUrl +
          this.bedrooms +
          "%3Fsearch_distance%3D0%26postal%3D" +
          this.zip_codes +
          "%26min_price%3D%26max_price%3D%26availabilityMode%3D0%26sale_date%3Dall%2Bdates",
        headers: {
          Accept: "application/json",
        },
        method: "get",
      }).then((res) => {
        console.log({ "this in .then": this });
        this.rooms = res.data;
        outputs = JSON.parse(JSON.stringify(this.rooms));
        console.log(outputs);
        this.rooms = JSON.parse(JSON.stringify(outputs.data.values));
        console.log(rooms);
      });
    },
  },
};

const app = Vue.createApp(App);

app.mount("#app");
