<template>
    <div class="settings-modal">
        <h1>Settings</h1>
        <form>
            <div class="form-group">
                <label for="setting1">Setting 1:</label>
                <input type="text" id="setting1" name="setting1">
            </div>
            <div class="form-group">
                <label for="setting2">Setting 2:</label>
                <select id="setting2" name="setting2">
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                </select>
            </div>
            <button type="submit">Save</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'Settings',
    data() {
        return {
            // Your settings data here
        };
    },
    methods: {
        // Methods for handling settings
    }
}
</script>

<style scoped>
.settings-modal {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    width: 300px;
    margin: auto;
    background-color: #f9f9f9;
}

.settings-modal h1 {
    text-align: center;
    color: #333;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    border: none;
    border-radius: 4px;
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}
</style>