<script>
export default {
    name: "MessageComponent",
    props: {
        browserUsername: {
            type: String,
            required: true,
        },
        messageUsername: {
            type: String,
            required: true,
        },
        message: {
            type: String,
            required: true,
        },
        timestamp: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            owner: false,
        };
    },
    mounted() {
        if (this.browserUsername === this.messageUsername) {
            this.owner = true;
        }
    },
};
</script>

<template>
    <div class="message" v-bind:class="owner ? 'ownerFloat' : ''">
        <div class="message-box" v-bind:class="owner ? 'ownerColor' : ''">
            {{ message }}
        </div>
        {{ messageUsername }} -
        {{ new Date(timestamp).toLocaleString() }}
    </div>
</template>

<style>
.message-box {
    padding: 5px;
    border-radius: 5px;
    background-color: lightblue;
}

.message {
    display: flex;
    flex-direction: column;
    margin: 10px 0;
    padding: 5px;
    border-radius: 5px;
    width: 250px;
}

.ownerColor {
    background-color: grey;
}

.ownerFloat {
    float: right;
}
</style>
