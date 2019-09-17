<template>
    <div id="app">
        <h1>Mu-ha-ha</h1> 

        <table>
            <thead>
                <tr>
                <th>id</th>
                <th>Mondat</th>
                </tr>
            </thead>
            <tbody>
                <tr v-bind:key="mondat" v-for="mondat in mondatok">
                    <td>{{mondat.id}}</td>
                    <td>{{mondat.content}}</td>
                </tr>
            </tbody>
        </table>  
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'MondatTest',
    data: function(){
        return {
            mondatok: []
        }
    },
    methods: {
        gyertekMondatok: function () {
            axios.get('http://localhost:5000/').then((response) => {
                this.mondatok = response.data;
            }, (error) => {
                console.log(error);
            });
        },
    },
    mounted: function () {
        this.gyertekMondatok();
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
