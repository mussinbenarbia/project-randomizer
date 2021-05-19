<script>
	import axios from "axios";
	import Technology from "./components/Technology.svelte"
	import Navbar from "./components/Navbar.svelte"
	import Footer from "./components/Footer.svelte"

	let allProjects = [];
	let projectData = {
		name: "",
		stack: [],
		cat: ""
	}
	
	const fetchProject = async () => {
		const {data: project} = await axios.get("/api/projects")
		allProjects = project;
		selectProject()
	}

	const selectProject = () => {
		projectData = allProjects[Math.floor(Math.random() * (allProjects.length -1))]
	}

	fetchProject()
	
</script>

<main>
	<Navbar/>
	<section>
		<h1>Your next project is...</h1>
	
		<h2>{projectData.name}</h2>
		
		<div class="stack">
			{#each projectData.stack as tech}
			<Technology techName={tech}/>
			{/each}
		</div>
		<button class="hover:bg-red-500 text-red-700 font-semibold hover:text-white py-2 px-4 border border-red-500 hover:border-transparent rounded" on:click={selectProject}>Randomize</button>
	</section>
	
	<Footer/>
</main>

<style>


	main {
		height: 100vh;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: space-between;
		
	}

	section {
		display: flex;
		flex-direction: column;
		align-items: center;
	}

	.stack {
		display: flex;
		justify-content: space-evenly;
		width: 500px;
		margin: 1rem;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
	h2 {
		text-transform: uppercase;
		font-size: 2em;
		font-weight: 300;
	}
	

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>