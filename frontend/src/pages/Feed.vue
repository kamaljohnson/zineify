<template>
	<div :style="'width: ' + cardWidth + 'px; height: ' + ( zineCardWidth + chatCardWidth + 50 ) + 'px;'">
		<Motion
			:animate="{x: [100, -50, 0]}"
			:exit="{x: [0, -100]}"
		>
			<Motion>
				<Card 
					title="How not to use #hashtags" 
					class="w-full" 
					:style="'height: ' + zineCardWidth + 'px;'" 
					@click="onZineCardClick()"
				>
					<span class="overflow-auto">
						"Ok, but what is a hashtag." is one of the most frequent questions we get. You don't have to master hashtags to love Twitter, but there is so much excitement to be found when you understand how to use them. In this article we explain how to get real business benefits out of hashtags.
					</span>
				</Card>
			</Motion>
			<Motion>
				<Card 
					class="my-5 pt-2 w-full" 
					:style="'height: ' + chatCardWidth + 'px;'" 
					@mouseover="expandChatCard()" 
					@mouseleave="shrinkChatCard()"
				>
					<div class="overflow-auto" :style="'height: ' + (chatCardWidth - 75) + 'px;'">
						<ListItem title="Kamal" subtitle="This is a really cool article, can you please share the link for getting more info on this please"></ListItem>
						<ListItem title="Aditya" subtitle="I don't know the original article, I got this from my friend 😅, But I dont think it would be really hard to get this, a simple google search will fetch you enough info"></ListItem>
						<ListItem title="Hey" subtitle="This is a message"></ListItem>
						<ListItem title="Hey" subtitle="This is a message"></ListItem>
						<ListItem title="Hey" subtitle="This is a message"></ListItem>
						<ListItem title="Hey" subtitle="This is a message"></ListItem>
					</div>
					<Input type="text" value="" placeholder="Type your message..." />
				</Card>
			</Motion>
		</Motion>
	</div>
</template>

<script>
import { Card, ListItem, Input } from 'frappe-ui'
import { Motion, Presence } from "motion/vue"

export default {
	name: 'Feed',
	props: ['feedId'],
	data() {
		return {
			chatCardWidth: 200,
			zineCardWidth: 350,
			cardWidth: 400,
			zineId: 0
		}
	},
	components: {
		Card,
		ListItem,
		Input,
		Motion,
		Presence,
	},
	methods: {
		expandChatCard() {
			this.chatCardWidth = 350;
			this.zineCardWidth = 200;
		},
		shrinkChatCard() {
			this.chatCardWidth = 200;
			this.zineCardWidth = 350;
		}
	}
}
</script>

<style>

</style>