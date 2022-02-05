<template>
	<div class="flex h-screen">
		<div class="m-auto">
			<Card title="Article Title" style="width: 400px;" :style="'height: ' + zineCardWidth + 'px;'" @click="onZineCardClick()">
				<span class="overflow-auto">
					Test Article means, in accordance with 21 C.F.R. § 50.3(j), any drug (including a biological product), medical device, food additive, color additive, electronic product, or any other article subject to regulation under the Federal Food, Drug, and Cosmetic Act that is intended for administration to humans or animals, including a drug or biologic as identified in the Research Plan and Appendix B, that is used within the scope of the Research Plan. The Test Article may also be referred to as Investigational Agent, Study Material, or Study Product.
				</span>
			</Card>
			<Card class="my-5 pt-2" style="width: 400px;" :style="'height: ' + chatCardWidth + 'px;'" @click="onChatCardClick()">
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
			<div>
				<Button class="float-left" icon="chevron-left"/>
				<Button class="float-right" icon="chevron-right"/>
			</div>
		</div>
	</div>
</template>

<script>
import { Card, ListItem, Input } from 'frappe-ui'

export default {
	name: 'Feeds',
	data() {
		return {
			chatCardWidth: 200,
			zineCardWidth: 400,
		}
	},
	components: {
		Card,
		ListItem,
		Input
	},
	methods: {
		onChatCardClick() {
			this.chatCardWidth = 350;
			this.zineCardWidth = 250;
		},
		onZineCardClick() {
			this.chatCardWidth = 200;
			this.zineCardWidth = 400;
		}
	}
}
</script>

<style>

</style>