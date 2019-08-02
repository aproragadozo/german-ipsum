<template>
  <div class="wrapper">
    <h1 class="title">German Ipsum</h1>
    <div class="box">
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    </div>
    <div class="controls">
      <input type="range" id="start" name="volume"
         min="0" max="11">
  <label for="volume">Volume</label>
  <div data-role="fieldcontain">
    <fieldset data-role="controlgroup" data-type="horizontal">
	    		<legend>HTML tag Wrapper</legend>

		     	<input type="radio" name="radio-choice-1" id="radio-choice-1" value="choice-1" checked="checked" />
		     	<label for="radio-choice-1">No Wrapper</label>

		     	<input type="radio" name="radio-choice-1" id="radio-choice-2" value="choice-2" />
		     	<label for="radio-choice-2">&lt;li&gt;</label>

		     	<input type="radio" name="radio-choice-1" id="radio-choice-3" value="choice-3" />
		     	<label for="radio-choice-3">&lt;p&gt;</label>
	    	</fieldset>
  </div>
    </div>
    <div class="go">
      <p>Mach schnell!</p>
    </div>
    <a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px" href="https://unsplash.com/@pear?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Pierre Gui"><span style="display:inline-block;padding:2px 3px"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-2px;fill:white" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M10 9V0h12v9H10zm12 5h10v18H0V14h10v9h12v-9z"></path></svg></span><span style="display:inline-block;padding:2px 3px">Pierre Gui</span></a>
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
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
}
  .title {
    font-size: 4em;
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
    font-size: 18px;
    color:midnightblue;
    width: 80%;
}
.controls {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background:crimson;
  width: 50vw;
  justify-self: flex-end;
  min-height: 10vh;
}
.go {
  text-transform: uppercase;
  background: rgb(32,184,120);
  color: whitesmoke;
  font-size: 2em;
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
</style>
