<script>
    async function getText() {
        let res = await fetch("/api/health");
        return await res.text();
    }
</script>

<h1>Welcome to SvelteKit</h1>
<p>
    Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation
</p>
<h3>{getText()}</h3>
