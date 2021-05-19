<script>
    export let techName;
    const capitalizeWord = (word) => word[0].toUpperCase()+word.slice(1) 

</script>

    <div class="tech">
        <img class="tech-img" src="./images/{techName}.svg" alt="tech">
        <h3>{capitalizeWord(techName)}</h3>
    </div>

<style>
    .tech {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .tech-img {
        width: 100px;
        height: 100px;
        margin-bottom: 0.5rem;
    }

    h3 {
		text-transform: uppercase;
		font-size: 1.2em;
		font-weight: 300;
	}
</style>