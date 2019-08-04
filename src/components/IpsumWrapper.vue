<template>
  <div class="wrapper">
    <h1 class="title">German Ipsum</h1>
    <div class="box">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </div>
    <div class="controls" data-role="fieldcontain">
      <fieldset data-role="controlgroup" data-type="horizontal">
        <label for="volume" style="display: inline-block; position:relative;">Number of sentences</label>
        <input type="range" id="start" name="volume" min="1" max="11" step="1" list="sentences">

        <datalist id="sentences">
          <option value="1" label="1"/>
          <option value="2" label="2"/>
          <option value="3" label="3"/>
          <option value="4" label="4"/>
          <option value="5" label="5"/>
          <option value="6" label="6"/>
          <option value="7" label="7"/>
          <option value="8" label="8"/>
          <option value="9" label="9"/>
          <option value="10" label="10"/>
        </datalist>
      </fieldset>
      <fieldset data-role="controlgroup" data-type="horizontal">
        <legend>HTML tag Wrapper</legend>
        <input type="radio"
          name="radio-choice-1"
          id="radio-choice-1" value="choice-1" checked="checked" />
        <label for="radio-choice-1">No Wrapper</label>
        <input type="radio" name="radio-choice-1" id="radio-choice-2" value="choice-2" />
        <label for="radio-choice-2">&lt;li&gt;</label>
        <input type="radio" name="radio-choice-1" id="radio-choice-3" value="choice-3" />
        <label for="radio-choice-3">&lt;p&gt;</label>
      </fieldset>
    </div>
    <div class="go">
      <p>Mach schnell!</p>
    </div>
    <a class="credit"
      href="https://unsplash.com/@pear?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge"
      target="_blank"
      rel="noopener noreferrer"
      title="Image credit: Unsplash">
      <span style="display:inline-block;padding:2px 3px">Pierre Gui</span>
    </a>
  </div>
</template>

<script>
export default {
  name: 'IpsumText',
};
</script>

<style>
.wrapper {
  width: 99vw;
  height: 99vh;
  background-image: url("../assets/snack.jpg");
  background-position: center;
  background-size: cover;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-direction: column;
}
.title {
    font-size: 4vmax;
    text-transform: uppercase;
    color: whitesmoke;
}
.box {
    max-height: 50vmax;
    width: 50vw;
    background: rgba(208,204,151,0.6);
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}
.box>p {
    opacity: 1;
    font-size: 1.5vmax;
    color:midnightblue;
    width: 80%;
}
.controls {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 50vw;
  justify-self: flex-end;
  min-height: 5vmin;
}
fieldset {
  border: none;
  position: relative;
  padding: 1em 0 1em 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;

  background:#dc143c99;
}
.go {
  text-transform: uppercase;
  background: rgb(32,184,120);
  color: whitesmoke;
  font-size: 2vmax;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30vw;
}
.go>p {
  width: 80%;
  text-align: center
}
a.credit{
  background-color:#333;
  color:white;
  text-decoration:none;
  padding:1px 3px;
  font-family:-apple-system, Helvetica, Arial, sans-serif;
  font-size:1.5vmin;
  font-weight:bold;
  line-height:1.2;
  display:inline-block;
  border-radius:3px;
}
</style>
