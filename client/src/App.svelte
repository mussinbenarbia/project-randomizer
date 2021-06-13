<script>
	import axios from "axios";
	import Technology from "./components/Technology.svelte";
	import Navbar from "./components/Navbar.svelte";
	import Footer from "./components/Footer.svelte";
	import uniqueRandom from "unique-random";
	
	let allProjects = [];
	let random;
	
	let currentProject = {
		name: "",
		stack: [],
		cat: ""
	}

	let nextProject = {
		name: "",
		stack: [],
		cat: ""
	}
	
	const fetchAllProjects = async () => {
		allProjects = (await axios.get("/api/projects")).data;	
	}

	const selectProject = () => {
		if (currentProject.name === ""){
			currentProject = allProjects[random()];
			nextProject = allProjects[random()];
		}else{
			currentProject = nextProject;
			nextProject = allProjects[random()];
		}		
	}

	const initializePage = async () => {
		await fetchAllProjects();
		random = uniqueRandom(0,(allProjects.length-1))
		selectProject();
	}
	
	initializePage();
	
</script>

<main>
	<Navbar/>
	<section>
		<h1>Your next project is...</h1>
	
		<h2>{currentProject.name}</h2>
		
		<div class="stack">
			{#each currentProject.stack as tech}
			<Technology techName={tech}/>
			{/each}
		</div>
		<button class="border-red-500 rounded text-red-700 font-semibold py-2 px-4 hover:bg-red-500 hover:text-white hover:border-transparent focus:border-red-500 focus:outline-none" on:click={selectProject}>Randomize</button>
	</section>
	<div class="next-stack">
		{#each nextProject.stack as tech}
		<Technology techName={tech}/>
		{/each}
	</div>
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

	.next-stack {
		display: none;
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