<template>
    <div id="app">
        <div v-if="!signedIn">
            <SignIn :value="userName" @inputChange="updateUserName" />
        </div>
        <div class="content" v-else>
            <MessagePage :userName="userName" />
        </div>
    </div>
</template>

<script>
import SignIn from "./components/SignIn.vue";
import MessagePage from "./components/MessagePage.vue";

export default {
    name: "App",
    components: {
        SignIn,
        MessagePage,
    },
    data() {
        return {
            userName: "",
            signedIn: false,
        };
    },
    methods: {
        updateUserName(newUserName) {
            this.userName = newUserName;
            this.signedIn = true;
            console.log("Users Name: " + this.userName);
        },
    },
};
</script>

<style>
.content {
    margin: 0 auto;
    width: 50%;
    border: 1px solid black;
    padding: 10px;
}
</style>
