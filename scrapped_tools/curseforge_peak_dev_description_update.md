# **4+ Months Later…**

## **<span style="color:#2dc26b">I've finally made public this alpha version of the</span> <span style="color:#f1c40f">PEAK</span> <span style="color:#2dc26b">modpack!</span>**

> ### ⚡ **Playing on a Laptop or Low-End PC? Try PEAK Lite!**
> Experiencing frame drops or have integrated graphics? Download **[👉 PEAK Lite](https://www.curseforge.com/minecraft/modpacks/peak-lite)**! It delivers identical gameplay, quests, recipes, and full multiplayer cross-play with this edition, but stripped of heavy particle engines, bloom shaders, and 3D leaves for maximum FPS at ~5–6 GB RAM!

***

###### **<span style="color:#2dc26b"><br></span>__What you see here is not the whole content! __File is UP!____**

After more than <span style="color:#f1c40f"><strong>4 months</strong></span> of building, rewriting configs, and over <span style="color:#f1c40f"><strong>280 hours</strong></span> of actual in-game testing and playtesting, the first public alpha of PEAK is finally out!

![PEAK Logo](https://media.forgecdn.net/attachments/2021/65/peak_logo_under_2mb_curseforge-gif.gif)

Before getting into what is in the pack, I want to talk about performance first. A lot of modern 1.21 modpacks run poorly or stutter because people just toss 300 mods into a folder and hope for the best. For PEAK, I spent back-breaking hours doing deep optimization: stripping out redundant mod bloat, unifying tags so you do not get three conflicting types of copper or random duplicate ingots, tuning garbage collection flags, and fixing structure leaks so chunks load when you are moving fast.

Because of everything that is packed into the world, **you will need to allocate at least <span style="color:#2dc26b">7 GB of free RAM</span>** in your launcher. Anything less and Java will choke on garbage collection. BUT, if you need a lightweight version that runs on **<span style="color:#2dc26b">5 to 6 GB RAM</span>**, grab **[👉 PEAK Lite](https://www.curseforge.com/minecraft/modpacks/peak-lite)** for the exact same gameplay with stripped visual overhead!

***

### **<span style="color:#2dc26b">So what is</span> <span style="color:#f1c40f">PEAK</span><span style="color:#2dc26b">?</span>**

![Creative Inventory](https://media.forgecdn.net/attachments/2021/46/creative_inventory_clean_cropped_curseforge-gif.gif)

At its heart, <span style="color:#f1c40f">PEAK</span> is a Create-centered pack, but stacked with addons and a ton of wild magic and tech content surrounding it.

I did not want this to feel like another one of those packs that holds your hand or forces you into a single linear checklist where you are just following lines on a screen. If you want to dive straight into kinetics and build automated factories, you can. If you want to mess with spells, go spelunking in deep caves, or build cozy farms, you can do that instead. There are multiple ways to solve almost every problem or automate materials!

***

### **<span style="color:#2dc26b">A funny twist on End gating</span>**

You cannot just speedrun the End on day two by crafting Eyes of Ender with blaze powder and pearls like vanilla. Stronghold access has a bit of custom gating:

To get your hands on Eyes of Ender, you actually have to go out into the world and get into some fights with bosses **(Check the boss questlines)** and dungeon threats. Once you go through the end portal and get your first taste of the End, you can take End Stone, crush it down into End Stone Powder, and use that to craft more eyes yourself!!! It gives exploring and fighting a real purpose rather than just ignoring everything on the surface.

![End Gating](https://media.forgecdn.net/attachments/description/1731360/description_c7a9289b-5ee9-4d4e-82bc-8450482cb2d8.png)

***

### <span style="color:#2dc26b"><strong>Quests, space travel, and everything in between</strong></span>

The questlines are inspired by packs like MC Eternal:

They are there to give you ideas, fun facts, survival tips, and rewards, not to force you down a tunnel. You get custom reward coffers, early game field guides, and secrets on how to stretch your resources.

![Quests Showcase 1](https://media.forgecdn.net/attachments/description/1731360/description_9e52d77e-6754-48c0-9d51-d4b7dfb95a98.png)

![Quests Showcase 2](https://media.forgecdn.net/attachments/description/1731360/description_a21f1dd0-a5e8-4d59-a3b1-0f43616a6b79.gif)

And once you get far enough into the machinery, you can build rockets, launch into orbit, and explore outside the Overworld.

***

# <span style="color:#2dc26b"><strong>This is an Alpha — I need your feedback!</strong></span>

![Panoramic Views](https://media.forgecdn.net/attachments/2021/81/3_views_under_2mb_curseforge-gif.gif)

This is the very first public release. I have put manyyy hours into balancing recipes, drop rates, and performance, but the best way to polish a pack is having real players jump in, try weird builds, and see what breaks.

If you run into bugs, weird recipe conflicts, or things that feel too grindy or too easy, please let me know and leave feedback. **<span style="color:#2dc26b">Your thoughts directly shape the next updates.</span>**

Jump in, build something cool, and <span style="color:#2dc26b"><strong>let me know what you think!!!</strong></span>

**Recommended Java Arguments:**

```
-XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=100 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=16m -XX:G1ReservePercent=15 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=8
```
