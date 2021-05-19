<script>
	import axios from "axios";
	import Technology from "./components/Technology.svelte"

	let projectData = {
		name: "",
		stack: [],
		cat: ""
	}
	
	const fetchProject = (async () => {
		const {data: project} = await axios.get("http://localhost:5000/api/projects")
		const randProject = project[Math.round(Math.random() * project.length)];
		return projectData = randProject
	})

	fetchProject()
	
</script>

<main>
	<h1>Your next project is...</h1>
	
	<h2>{projectData.name}</h2>
	
	<div class="stack">
		{#each projectData.stack as tech}
		<Technology techName={tech}/>
		{/each}
	</div>
	<button on:click={fetchProject}>Randomize</button>
</main>

<style>


	main {
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 1em;
	}

	.stack {
		display: flex;
		justify-content: space-evenly;
		width: 500px;
		margin: 2rem;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>