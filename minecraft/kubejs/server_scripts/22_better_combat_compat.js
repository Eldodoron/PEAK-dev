// Adds Better Combat animations to weapons that lack them

ServerEvents.highPriorityData(event => {
    // Make The Blood Harvester attack like a Scythe
    event.addJson('simplymore:weapon_attributes/the_blood_harvester', {
        "parent": "bettercombat:scythe",
        "attributes": {
            "category": "scythe",
            "two_handed": true,
            "range_bonus": 1.0
        }
    });
});
